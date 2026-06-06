import { useState, useEffect, useMemo } from 'react';
import './App.css';
import rawProblems from './data/problems.json';
import NeetCodeDashboard from './NeetCodeDashboard';

interface Problem {
  id: number;
  title: string;
  zerojudge_url: string;
  uva_url: string;
  problem_num: string;
  zerojudge_id: string;
  source: string;
}

type SolveStatus = 'todo' | 'in-progress' | 'solved';

export default function App() {
  const problems = rawProblems as Problem[];

  // States
  const [activeTab, setActiveTab] = useState<'cpe' | 'neetcode'>('cpe');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedPlatform, setSelectedPlatform] = useState<'all' | 'ZeroJudge' | 'VJudge'>('all');
  const [selectedStatus, setSelectedStatus] = useState<'all' | SolveStatus>('all');
  const [sortBy, setSortBy] = useState<'num-asc' | 'num-desc' | 'title-asc' | 'title-desc'>('num-asc');
  const [viewMode, setViewMode] = useState<'table' | 'grid'>('table');
  const [theme, setTheme] = useState<'dark' | 'light'>('dark');
  
  // Selection states for batch operations
  const [selectedIds, setSelectedIds] = useState<number[]>([]);

  // LocalStorage state for progress tracking
  const [solveStates, setSolveStates] = useState<Record<number, SolveStatus>>(() => {
    try {
      const saved = localStorage.getItem('cpe-solve-states');
      return saved ? JSON.parse(saved) : {};
    } catch {
      return {};
    }
  });

  // Save to localStorage
  useEffect(() => {
    localStorage.setItem('cpe-solve-states', JSON.stringify(solveStates));
  }, [solveStates]);

  // Toggle Theme
  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
  }, [theme]);

  // Reset selected IDs when filter conditions change
  useEffect(() => {
    setSelectedIds([]);
  }, [searchQuery, selectedPlatform, selectedStatus]);

  // Handle single status change
  const handleStatusChange = (id: number, status: SolveStatus) => {
    setSolveStates(prev => ({
      ...prev,
      [id]: status
    }));
  };

  // Stats calculation
  const stats = useMemo(() => {
    const total = problems.length;
    let solved = 0;
    let inProgress = 0;
    let todo = 0;
    let zjCount = 0;
    let vjCount = 0;

    problems.forEach(p => {
      const status = solveStates[p.id] || 'todo';
      if (status === 'solved') solved++;
      else if (status === 'in-progress') inProgress++;
      else todo++;

      if (p.source === 'ZeroJudge') zjCount++;
      else vjCount++;
    });

    return {
      total,
      solved,
      inProgress,
      todo,
      zjCount,
      vjCount,
      solvedPercent: total > 0 ? Math.round((solved / total) * 100) : 0,
      inProgressPercent: total > 0 ? Math.round((inProgress / total) * 100) : 0,
    };
  }, [problems, solveStates]);

  // Reset progress helper
  const handleReset = () => {
    if (window.confirm('確定要重置所有題目狀態嗎？此動作無法復原。')) {
      setSolveStates({});
      setSelectedIds([]);
    }
  };

  // Filtered and Sorted Problems
  const filteredProblems = useMemo(() => {
    return problems
      .filter(p => {
        // Search filter (ID, Title, Problem Number, ZeroJudge ID)
        const query = searchQuery.toLowerCase().trim();
        const matchesSearch = 
          p.title.toLowerCase().includes(query) ||
          p.problem_num.toLowerCase().includes(query) ||
          p.zerojudge_id.toLowerCase().includes(query) ||
          p.id.toString() === query;

        // Platform filter
        const matchesPlatform = 
          selectedPlatform === 'all' || 
          p.source === selectedPlatform;

        // Status filter
        const currentStatus = solveStates[p.id] || 'todo';
        const matchesStatus = 
          selectedStatus === 'all' || 
          currentStatus === selectedStatus;

        return matchesSearch && matchesPlatform && matchesStatus;
      })
      .sort((a, b) => {
        // Sorting logic
        const numA = parseInt(a.problem_num, 10) || 0;
        const numB = parseInt(b.problem_num, 10) || 0;

        if (sortBy === 'num-asc') return numA - numB;
        if (sortBy === 'num-desc') return numB - numA;
        
        if (sortBy === 'title-asc') return a.title.localeCompare(b.title);
        if (sortBy === 'title-desc') return b.title.localeCompare(a.title);

        return 0;
      });
  }, [problems, searchQuery, selectedPlatform, selectedStatus, sortBy, solveStates]);

  // Selection toggle handlers
  const handleToggleSelect = (id: number) => {
    setSelectedIds(prev => 
      prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]
    );
  };

  const handleSelectAllVisible = (checked: boolean) => {
    if (checked) {
      setSelectedIds(filteredProblems.map(p => p.id));
    } else {
      setSelectedIds([]);
    }
  };

  const isAllVisibleSelected = useMemo(() => {
    return filteredProblems.length > 0 && 
      filteredProblems.every(p => selectedIds.includes(p.id));
  }, [filteredProblems, selectedIds]);

  const handleBatchStatusChange = (status: SolveStatus) => {
    setSolveStates(prev => {
      const next = { ...prev };
      selectedIds.forEach(id => {
        next[id] = status;
      });
      return next;
    });
    setSelectedIds([]);
  };

  return (
    <div className={`app-container ${theme}`}>
      {/* Background blobs for premium glassmorphism feel */}
      <div className="bg-blob blob-1"></div>
      <div className="bg-blob blob-2"></div>
      <div className="bg-blob blob-3"></div>

      <header className="app-header">
        <div className="header-brand">
          <div className="logo-icon">
            <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <path d="M18 3a3 3 0 0 0-3 3v12a3 3 0 0 0 3 3 3 3 0 0 0 3-3V6a3 3 0 0 0-3-3z"/>
              <path d="M3 3a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3 3 3 0 0 1-3-3V6a3 3 0 0 1 3-3z"/>
              <path d="M9 3h6v18H9z"/>
            </svg>
          </div>
          <div>
            <h1>程式能力檢定追蹤看板</h1>
            <p className="subtitle">高效追蹤與管理您的程式能力檢定考古題</p>
          </div>
        </div>

        <div className="main-tabs">
          <button 
            className={`tab-btn ${activeTab === 'cpe' ? 'active' : ''}`}
            onClick={() => setActiveTab('cpe')}
          >
            CPE 題目
          </button>
          <button 
            className={`tab-btn ${activeTab === 'neetcode' ? 'active' : ''}`}
            onClick={() => setActiveTab('neetcode')}
          >
            NeetCode 150
          </button>
        </div>

        <div className="header-actions">
          <button 
            className="btn-icon theme-toggle" 
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
            title={theme === 'dark' ? '切換為亮色模式' : '切換為暗色模式'}
          >
            {theme === 'dark' ? (
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <circle cx="12" cy="12" r="5" />
                <path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" />
              </svg>
            ) : (
              <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
              </svg>
            )}
          </button>
          {activeTab === 'cpe' && (
            <button className="btn-secondary btn-reset" onClick={handleReset}>
              重置進度
            </button>
          )}
        </div>
      </header>

      {activeTab === 'cpe' ? (
        <>
      {/* Stats Dashboard Grid */}
      <section className="stats-grid">
        <div className="stats-card progress-card">
          <div className="stats-card-header">
            <h3>整體完成度</h3>
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
            <div className="value-num">{stats.zjCount}</div>
            <div className="value-label">ZeroJudge 題目</div>
          </div>
          <div className="value-divider"></div>
          <div className="value-item">
            <div className="value-num">{stats.vjCount}</div>
            <div className="value-label">UVa / VJudge</div>
          </div>
        </div>
      </section>

      {/* Controls Container */}
      <section className="controls-container">
        {/* Search Bar */}
        <div className="search-box">
          <svg className="search-icon" viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.3-4.3" />
          </svg>
          <input 
            type="text" 
            placeholder="搜尋題目名稱、UVA 編號、ZeroJudge ID..." 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
          {searchQuery && (
            <button className="clear-search" onClick={() => setSearchQuery('')}>
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M18 6 6 18M6 6l12 12" />
              </svg>
            </button>
          )}
        </div>

        {/* Filters and Sorting */}
        <div className="filters-group">
          <div className="filter-select-wrapper">
            <label>來源平台</label>
            <div className="segmented-control">
              <button className={selectedPlatform === 'all' ? 'active' : ''} onClick={() => setSelectedPlatform('all')}>全部</button>
              <button className={selectedPlatform === 'ZeroJudge' ? 'active' : ''} onClick={() => setSelectedPlatform('ZeroJudge')}>ZeroJudge</button>
              <button className={selectedPlatform === 'VJudge' ? 'active' : ''} onClick={() => setSelectedPlatform('VJudge')}>UVa / VJudge</button>
            </div>
          </div>

          <div className="filter-select-wrapper">
            <label>狀態篩選</label>
            <div className="segmented-control">
              <button className={selectedStatus === 'all' ? 'active' : ''} onClick={() => setSelectedStatus('all')}>全部</button>
              <button className={selectedStatus === 'todo' ? 'active' : ''} onClick={() => setSelectedStatus('todo')}>未開始</button>
              <button className={selectedStatus === 'in-progress' ? 'active' : ''} onClick={() => setSelectedStatus('in-progress')}>學習中</button>
              <button className={selectedStatus === 'solved' ? 'active' : ''} onClick={() => setSelectedStatus('solved')}>已解決</button>
            </div>
          </div>

          <div className="filter-select-wrapper">
            <label>排序方式</label>
            <select value={sortBy} onChange={(e) => setSortBy(e.target.value as any)} className="dropdown-select">
              <option value="num-asc">題號 (從小到大)</option>
              <option value="num-desc">題號 (從大到小)</option>
              <option value="title-asc">題目名稱 (A-Z)</option>
              <option value="title-desc">題目名稱 (Z-A)</option>
            </select>
          </div>

          <div className="view-toggle-wrapper">
            <label>版面模式</label>
            <div className="view-toggle">
              <button 
                className={viewMode === 'table' ? 'active' : ''} 
                onClick={() => setViewMode('table')}
                title="表格視圖"
              >
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M3 3h18v18H3zM3 9h18M3 15h18M12 3v18" />
                </svg>
              </button>
              <button 
                className={viewMode === 'grid' ? 'active' : ''} 
                onClick={() => setViewMode('grid')}
                title="卡片視圖"
              >
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                  <rect x="3" y="3" width="7" height="7" />
                  <rect x="14" y="3" width="7" height="7" />
                  <rect x="14" y="14" width="7" height="7" />
                  <rect x="3" y="14" width="7" height="7" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Results Count Banner */}
      <div className="results-banner">
        找到 <strong>{filteredProblems.length}</strong> 筆符合條件的題目
      </div>

      {/* Main Problems Presentation */}
      <main className="content-area">
        {filteredProblems.length === 0 ? (
          <div className="empty-state">
            <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10" />
              <path d="M8 12h8M12 8v8" />
            </svg>
            <h3>沒有找到符合篩選條件的題目</h3>
            <p>請嘗試修改您的搜尋關鍵字或篩選條件。</p>
          </div>
        ) : viewMode === 'table' ? (
          <div className="table-responsive">
            <table className="problems-table">
              <thead>
                <tr>
                  <th style={{ width: '40px', textAlign: 'center' }}>
                    <input 
                      type="checkbox" 
                      className="custom-checkbox"
                      checked={isAllVisibleSelected} 
                      onChange={(e) => handleSelectAllVisible(e.target.checked)}
                      title="全選此頁面所有題目"
                    />
                  </th>
                  <th>編號</th>
                  <th>UVA 題號</th>
                  <th style={{ width: '40%' }}>題目名稱</th>
                  <th>ZeroJudge ID</th>
                  <th>線上練習連結</th>
                  <th style={{ width: '150px' }}>進度狀態</th>
                </tr>
              </thead>
              <tbody>
                {filteredProblems.map((p) => {
                  const status = solveStates[p.id] || 'todo';
                  const isSelected = selectedIds.includes(p.id);
                  return (
                    <tr key={p.id} className={`status-row-${status} ${isSelected ? 'row-selected' : ''}`}>
                      <td style={{ textAlign: 'center' }}>
                        <input 
                          type="checkbox" 
                          className="custom-checkbox"
                          checked={isSelected} 
                          onChange={() => handleToggleSelect(p.id)}
                        />
                      </td>
                      <td className="col-id">{p.id}</td>
                      <td>
                        <span className="badge-problem-num">
                          {p.problem_num}
                        </span>
                      </td>
                      <td className="col-title">
                        <div className="title-text">{p.title}</div>
                      </td>
                      <td>
                        {p.zerojudge_id ? (
                          <span className="badge-zj-id">{p.zerojudge_id}</span>
                        ) : (
                          <span className="badge-zj-id empty">-</span>
                        )}
                      </td>
                      <td className="col-links">
                        <div className="link-buttons">
                          {p.zerojudge_url && (
                            <a 
                              href={p.zerojudge_url} 
                              target="_blank" 
                              rel="noreferrer" 
                              className={`link-btn platform-${p.source}`}
                            >
                              {p.source}
                            </a>
                          )}
                          {p.uva_url && (
                            <a 
                              href={p.uva_url} 
                              target="_blank" 
                              rel="noreferrer" 
                              className="link-btn platform-pdf"
                            >
                              PDF 題目
                            </a>
                          )}
                        </div>
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
        ) : (
          <div className="problems-grid">
            {filteredProblems.map((p) => {
              const status = solveStates[p.id] || 'todo';
              const isSelected = selectedIds.includes(p.id);
              return (
                <div key={p.id} className={`problem-card status-border-${status} ${isSelected ? 'card-selected' : ''}`}>
                  <div className="card-top">
                    <div className="card-top-left">
                      <input 
                        type="checkbox" 
                        className="custom-checkbox card-select-checkbox"
                        checked={isSelected} 
                        onChange={() => handleToggleSelect(p.id)}
                      />
                      <span className="card-id">#{p.id}</span>
                    </div>
                    <span className="card-platform">{p.source}</span>
                  </div>
                  
                  <div className="card-middle">
                    <div className="card-num">{p.problem_num}</div>
                    <h4 className="card-title">{p.title}</h4>
                    {p.zerojudge_id && (
                      <div className="card-zj-info">
                        ZeroJudge ID: <strong>{p.zerojudge_id}</strong>
                      </div>
                    )}
                  </div>

                  <div className="card-links">
                    {p.zerojudge_url && (
                      <a href={p.zerojudge_url} target="_blank" rel="noreferrer" className="card-link-btn primary">
                        線上練習 ({p.source})
                      </a>
                    )}
                    {p.uva_url && (
                      <a href={p.uva_url} target="_blank" rel="noreferrer" className="card-link-btn secondary">
                        原題 PDF
                      </a>
                    )}
                  </div>

                  <div className="card-status-control">
                    <button 
                      className={`status-btn-option todo ${status === 'todo' ? 'active' : ''}`}
                      onClick={() => handleStatusChange(p.id, 'todo')}
                    >
                      未開始
                    </button>
                    <button 
                      className={`status-btn-option in-progress ${status === 'in-progress' ? 'active' : ''}`}
                      onClick={() => handleStatusChange(p.id, 'in-progress')}
                    >
                      學習中
                    </button>
                    <button 
                      className={`status-btn-option solved ${status === 'solved' ? 'active' : ''}`}
                      onClick={() => handleStatusChange(p.id, 'solved')}
                    >
                      已解決
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </main>

      {/* Floating Batch Action Bar */}
      {selectedIds.length > 0 && (
        <div className="batch-action-bar">
          <div className="batch-action-content">
            <span className="batch-selected-count">
              已選取 <strong>{selectedIds.length}</strong> 題
            </span>
            <div className="batch-action-buttons">
              <button 
                className="batch-btn batch-btn-solved" 
                onClick={() => handleBatchStatusChange('solved')}
              >
                標記已解決
              </button>
              <button 
                className="batch-btn batch-btn-progress" 
                onClick={() => handleBatchStatusChange('in-progress')}
              >
                標記學習中
              </button>
              <button 
                className="batch-btn batch-btn-todo" 
                onClick={() => handleBatchStatusChange('todo')}
              >
                標記未開始
              </button>
              <button 
                className="batch-btn-cancel" 
                onClick={() => setSelectedIds([])}
              >
                取消選取 ({selectedIds.length})
              </button>
            </div>
          </div>
        </div>
      )}
        </>
      ) : (
        <NeetCodeDashboard theme={theme} />
      )}

      <footer className="app-footer">
        <p>© 2026 CPE 題目練習追蹤看板 • 採用 React 與 TypeScript 開發</p>
      </footer>
    </div>
  );
}
