import './example.css';

export function GlassmorphismHero() {
  return (
    <section className="glass-demo" aria-labelledby="glass-title">
      {/* Responsive intent: the layout remains content-driven and can stack at compact widths. */}
      <article className="glass-card">
        <h2 id="glass-title">Focus mode</h2>
        <p>The glass is bounded to a card and has an opaque fallback for unsupported browsers.</p>
        <button className="glass-button" type="button" data-state="ready">Enable focus mode</button>
      </article>
    </section>
  );
}
