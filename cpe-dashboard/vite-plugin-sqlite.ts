import type { Plugin } from 'vite';
import Database from 'better-sqlite3';

export function sqliteProgressPlugin(): Plugin {
  return {
    name: 'sqlite-progress-plugin',
    configureServer(server) {
      // Initialize DB
      const db = new Database('progress.db');
      
      // Create table if not exists
      // platform: 'cpe' or 'neetcode'
      // id: problem id (number)
      // status: 'todo' | 'in-progress' | 'solved'
      db.exec(`
        CREATE TABLE IF NOT EXISTS progress (
          platform TEXT,
          id INTEGER,
          status TEXT,
          PRIMARY KEY (platform, id)
        )
      `);

      // Add middlewares to intercept API calls
      server.middlewares.use('/api/progress', (req, res, next) => {
        if (req.method === 'GET') {
          try {
            const stmt = db.prepare('SELECT platform, id, status FROM progress');
            const rows = stmt.all();
            
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify(rows));
          } catch (err: any) {
            res.statusCode = 500;
            res.end(JSON.stringify({ error: err.message }));
          }
          return;
        }

        if (req.method === 'POST') {
          let body = '';
          req.on('data', chunk => {
            body += chunk.toString();
          });
          req.on('end', () => {
            try {
              const { platform, id, status } = JSON.parse(body);
              
              if (!platform || id === undefined || !status) {
                res.statusCode = 400;
                res.end(JSON.stringify({ error: 'Missing parameters' }));
                return;
              }

              const stmt = db.prepare(`
                INSERT INTO progress (platform, id, status)
                VALUES (?, ?, ?)
                ON CONFLICT(platform, id) DO UPDATE SET status=excluded.status
              `);
              stmt.run(platform, id, status);
              
              res.setHeader('Content-Type', 'application/json');
              res.end(JSON.stringify({ success: true }));
            } catch (err: any) {
              res.statusCode = 500;
              res.end(JSON.stringify({ error: err.message }));
            }
          });
          return;
        }

        if (req.method === 'DELETE') {
          const url = new URL(req.url || '', `http://${req.headers.host}`);
          const platform = url.searchParams.get('platform');
          if (platform) {
            try {
              const stmt = db.prepare('DELETE FROM progress WHERE platform = ?');
              stmt.run(platform);
              res.setHeader('Content-Type', 'application/json');
              res.end(JSON.stringify({ success: true }));
            } catch (err: any) {
              res.statusCode = 500;
              res.end(JSON.stringify({ error: err.message }));
            }
          } else {
            res.statusCode = 400;
            res.end(JSON.stringify({ error: 'Missing platform' }));
          }
          return;
        }

        next();
      });
    }
  };
}
