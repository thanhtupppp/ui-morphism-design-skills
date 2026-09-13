import './example.css';

export function OperationsBento() {
  return (
    <main className="bento-grid" aria-labelledby="operations-title">
      <article className="bento-card bento-card--hero">
        <p>Overview</p>
        <h1 id="operations-title">Operations</h1>
        <p>Primary task and key metric receive the largest area.</p>
        <button className="bento-action" type="button">Open dashboard</button>
      </article>

      <article className="bento-card bento-card--wide" aria-labelledby="energy-title">
        <p>Today</p>
        <h2 id="energy-title">Energy usage</h2>
        <p>24.8 kWh</p>
      </article>

      <article className="bento-card bento-card--supporting" aria-labelledby="alerts-title">
        <p>Status</p>
        <h2 id="alerts-title">Alerts</h2>
        <p>3 open</p>
        <button className="bento-action" type="button">Review alerts</button>
      </article>

      <article className="bento-card bento-card--utility" aria-labelledby="uptime-title">
        <p>Service</p>
        <h2 id="uptime-title">Uptime</h2>
        <p>99.9%</p>
      </article>
    </main>
  );
}
