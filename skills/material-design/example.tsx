import './example.css';

export function MaterialCard() {
  return (
    <section className="material-demo" aria-labelledby="material-title">
      {/* Responsive intent: compact widths switch the card and action to a stacked layout. */}
      <article className="material-card">
        <h2 id="material-title">System status</h2>
        <p>Elevation, state layers, and component states form a reusable system.</p>
        <button className="material-button" type="button" data-state="ready">Open status</button>
      </article>
    </section>
  );
}
