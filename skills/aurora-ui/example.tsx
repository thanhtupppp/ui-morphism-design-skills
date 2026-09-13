import './example.css';

export function AuroraHero() {
  return (
    <section className="aurora-demo" aria-labelledby="aurora-title">
      {/* Responsive intent: compact widths use reduced padding while content remains in reading order. */}
      <article className="aurora-card">
        <h2 id="aurora-title">Build with clarity</h2>
        <p>Aurora is atmosphere behind a stable content surface, not a replacement for hierarchy.</p>
        <button className="aurora-button" type="button" data-state="ready">Start building</button>
      </article>
    </section>
  );
}
