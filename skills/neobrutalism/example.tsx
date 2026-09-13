import './example.css';

export function NeobrutalismCard() {
  return (
    <section className="neo-demo" aria-labelledby="neo-title">
      {/* Responsive intent: the card remains content-driven and can stack at compact widths. */}
      <article className="neo-card">
        <h2 id="neo-title">Ship something bold</h2>
        <p>Hard borders and offset shadows create identity while semantic states stay conventional.</p>
        <button className="neo-button" type="button" data-state="ready">Create project</button>
      </article>
    </section>
  );
}
