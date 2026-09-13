import './example.css';

export function FlatDesignCard() {
  return (
    <section className="flat-demo" aria-labelledby="flat-demo-title">
      <div className="flat-shell">
        <nav className="flat-nav" aria-label="Primary navigation">
          <strong>Operations</strong>
          <div className="flat-nav__links">
            <a href="#overview" aria-current="page">Overview</a>
            <a href="#assets">Assets</a>
            <a href="#reports">Reports</a>
          </div>
        </nav>

        <main className="flat-main">
          <header>
            <h1 id="flat-demo-title">Operations overview</h1>
            <p>Hierarchy comes from type, spacing, grouping, borders, and explicit states.</p>
          </header>

          <div className="flat-grid" aria-label="Summary metrics">
            <article className="flat-card flat-card--summary">
              <strong>Active assets</strong>
              <span>128</span>
              <span className="flat-badge">Healthy</span>
            </article>
            <article className="flat-card flat-card--summary">
              <strong>Open work orders</strong>
              <span>14</span>
              <span className="flat-chip">Needs review</span>
            </article>
            <article className="flat-card flat-card--summary">
              <strong>Completion</strong>
              <progress className="flat-progress" value={82} max={100}>82%</progress>
              <span>82%</span>
            </article>
          </div>

          <div className="flat-alert flat-alert--success" role="status">
            <strong>System status:</strong> All critical services are operational.
          </div>

          <section className="flat-panel" aria-labelledby="filters-title">
            <h2 id="filters-title">Filters</h2>
            <div className="flat-grid">
              <div className="flat-field">
                <label htmlFor="asset-search">Search assets</label>
                <input className="flat-input" id="asset-search" name="asset-search" type="search" placeholder="Asset name or ID" />
              </div>
              <div className="flat-field">
                <label htmlFor="asset-status">Status</label>
                <select className="flat-select" id="asset-status" name="asset-status" defaultValue="all">
                  <option value="all">All statuses</option>
                  <option value="healthy">Healthy</option>
                  <option value="attention">Needs attention</option>
                </select>
              </div>
              <div className="flat-actions">
                <button className="flat-button" type="button">Apply filters</button>
                <button className="flat-button flat-button--secondary" type="button">Reset</button>
              </div>
            </div>
          </section>

          <section className="flat-panel" aria-labelledby="assets-title">
            <h2 id="assets-title">Recent assets</h2>
            <div className="flat-table-wrap">
              <table className="flat-table">
                <caption>Recent asset status</caption>
                <thead>
                  <tr><th scope="col">Asset</th><th scope="col">Location</th><th scope="col">Status</th><th scope="col">Action</th></tr>
                </thead>
                <tbody>
                  <tr><th scope="row">AHU-104</th><td>Building A</td><td><span className="flat-badge">Healthy</span></td><td><button className="flat-button flat-button--secondary" type="button">View</button></td></tr>
                  <tr><th scope="row">FCU-207</th><td>Building B</td><td><span className="flat-badge">Attention</span></td><td><button className="flat-button flat-button--secondary" type="button">Review</button></td></tr>
                </tbody>
              </table>
            </div>
          </section>

          <section className="flat-panel" aria-labelledby="tabs-title">
            <h2 id="tabs-title">Details</h2>
            <div className="flat-tabs" role="tablist" aria-label="Asset details">
              <button className="flat-tab" type="button" role="tab" aria-selected="true">Overview</button>
              <button className="flat-tab" type="button" role="tab" aria-selected="false">History</button>
            </div>
          </section>

          <div className="flat-empty" hidden>
            No assets match the selected filters.
          </div>
        </main>
      </div>
    </section>
  );
}
