import { useState, useEffect, useMemo } from 'react';
import rawProblems from './data/neetcode150.json';
import './App.css'; // Reuse styles

interface NeetCodeProblem {
  id: number;
  title: string;
  category: string;
  difficulty: string;
  leetcode_url: string;
}

type SolveStatus = 'todo' | 'in-progress' | 'solved';

export default function NeetCodeDashboard({ theme }: { theme: 'dark' | 'light' }) {
  const problems = rawProblems as NeetCodeProblem[];

  // Load from SQLite on mount
  const [solveStates, setSolveStates] = useState<Record<number, SolveStatus>>({});

  useEffect(() => {
    fetch('/api/progress')
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data)) {
          const loadedStates: Record<number, SolveStatus> = {};
          data.forEach(row => {
            if (row.platform === 'neetcode') {
              loadedStates[row.id] = row.status as SolveStatus;
            }
          });
          setSolveStates(loadedStates);
        }
      })
      .catch(err => console.error('Failed to load progress from SQLite:', err));
  }, []);

  const handleStatusChange = (id: number, status: SolveStatus) => {
    setSolveStates(prev => ({
      ...prev,
      [id]: status
    }));

    // Save to SQLite
    fetch('/api/progress', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ platform: 'neetcode', id, status })
    }).catch(err => console.error('Failed to save progress to SQLite:', err));
  };

  // Group by category
  const categoriesOrder = [
    "Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search",
    "Linked List", "Trees", "Heap / Priority Queue", "Backtracking", "Tries",
    "Graphs", "Advanced Graphs", "1-D Dynamic Programming", "2-D Dynamic Programming",
    "Greedy", "Intervals", "Math & Geometry", "Bit Manipulation"
  ];

  // Collapse state for categories (default to collapsed)
  const [collapsedCats, setCollapsedCats] = useState<Record<string, boolean>>(() => {
    const initial: Record<string, boolean> = {};
    categoriesOrder.forEach(cat => initial[cat] = true);
    return initial;
  });

  const toggleCategory = (cat: string) => {
    setCollapsedCats(prev => ({ ...prev, [cat]: !prev[cat] }));
  };

  const groupedProblems = useMemo(() => {
    const groups: Record<string, NeetCodeProblem[]> = {};
    categoriesOrder.forEach(cat => groups[cat] = []);
    
    problems.forEach(p => {
      if (groups[p.category]) {
        groups[p.category].push(p);
      } else {
        // Fallback for unexpected categories
        if (!groups['Other']) groups['Other'] = [];
        groups['Other'].push(p);
      }
    });
    return groups;
  }, [problems]);

  // Overall stats
  const stats = useMemo(() => {
    const total = problems.length;
    let solved = 0;
    let inProgress = 0;
    let todo = 0;

    problems.forEach(p => {
      const status = solveStates[p.id] || 'todo';
      if (status === 'solved') solved++;
      else if (status === 'in-progress') inProgress++;
      else todo++;
    });

    return {
      total,
      solved,
      inProgress,
      todo,
      solvedPercent: total > 0 ? Math.round((solved / total) * 100) : 0,
      inProgressPercent: total > 0 ? Math.round((inProgress / total) * 100) : 0,
    };
  }, [problems, solveStates]);

  return (
    <div className="neetcode-dashboard fade-in">
      {/* Stats Dashboard Grid */}
      <section className="stats-grid" style={{ marginBottom: '2rem' }}>
        <div className="stats-card progress-card">
          <div className="stats-card-header">
            <h3>NeetCode 150 完成度</h3>
            <span className="stats-badge highlight">{stats.solvedPercent}%</span>
          </div>
          <div className="progress-bar-container">
            <div className="progress-bar solved-bar" style={{ width: `${stats.solvedPercent}%` }}></div>
            <div className="progress-bar in-progress-bar" style={{ width: `${stats.inProgressPercent}%`, left: `${stats.solvedPercent}%` }}></div>
          </div>
          <div className="progress-details">
            <span className="dot solved">已解決 {stats.solved} 題</span>
            <span className="dot in-progress">學習中 {stats.inProgress} 題</span>
            <span className="dot todo">未開始 {stats.todo} 題</span>
          </div>
        </div>

        <div className="stats-card value-card">
          <div className="value-item">
            <div className="value-num">{stats.total}</div>
            <div className="value-label">總題目數量</div>
          </div>
          <div className="value-divider"></div>
          <div className="value-item">
            <div className="value-num">{stats.solved}</div>
            <div className="value-label">已征服</div>
          </div>
        </div>
      </section>

      {/* Grouped Problems List */}
      <div className="categories-container">
        {categoriesOrder.map(category => {
          const catProblems = groupedProblems[category];
          if (!catProblems || catProblems.length === 0) return null;
          
          const catSolved = catProblems.filter(p => solveStates[p.id] === 'solved').length;
          
          return (
            <div key={category} className="category-section">
              <div className="category-header collapse-header" onClick={() => toggleCategory(category)}>
                <div className="category-title-group">
                  <svg 
                    className={`collapse-icon ${collapsedCats[category] ? 'collapsed' : ''}`}
                    viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"
                  >
                    <polyline points="6 9 12 15 18 9"></polyline>
                  </svg>
                  <h3>{category}</h3>
                </div>
                <span className="category-count">({catSolved} / {catProblems.length})</span>
              </div>
              {!collapsedCats[category] && (
                <div className="table-responsive">
                  <table className="problems-table neetcode-table">
                    <thead>
                      <tr>
                        <th style={{ width: '60px' }}>ID</th>
                        <th style={{ width: '40%' }}>題目名稱</th>
                        <th style={{ width: '120px' }}>難度</th>
                        <th>LeetCode 連結</th>
                        <th style={{ width: '150px' }}>進度狀態</th>
                      </tr>
                    </thead>
                    <tbody>
                      {catProblems.map(p => {
                        const status = solveStates[p.id] || 'todo';
                        let diffClass = '';
                        if (p.difficulty === 'Easy') diffClass = 'diff-easy';
                        if (p.difficulty === 'Medium') diffClass = 'diff-medium';
                        if (p.difficulty === 'Hard') diffClass = 'diff-hard';

                        return (
                          <tr key={p.id} className={`status-row-${status}`}>
                            <td className="col-id">{p.id}</td>
                            <td className="col-title">
                              <div className="title-text">{p.title}</div>
                            </td>
                            <td>
                              <span className={`difficulty-badge ${diffClass}`}>
                                {p.difficulty}
                              </span>
                            </td>
                            <td className="col-links">
                              <a 
                                href={p.leetcode_url} 
                                target="_blank" 
                                rel="noreferrer" 
                                className="link-btn platform-leetcode"
                              >
                                LeetCode
                              </a>
                            </td>
                            <td>
                              <select 
                                value={status}
                                onChange={(e) => handleStatusChange(p.id, e.target.value as SolveStatus)}
                                className={`select-status status-${status}`}
                              >
                                <option value="todo">未開始</option>
                                <option value="in-progress">學習中</option>
                                <option value="solved">已解決</option>
                              </select>
                            </td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
