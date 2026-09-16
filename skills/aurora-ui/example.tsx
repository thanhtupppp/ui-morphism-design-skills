import './example.css';

export function AuroraHero({ effects = 'full', onStart }: { effects?: 'full' | 'off'; onStart?: () => void }) {
  return (
    <section className="aurora-demo" data-effects={effects} aria-labelledby="aurora-title">
      <article className="aurora-card">
        <h2 id="aurora-title">Create something remarkable</h2>
        <p>The Aurora layer adds atmosphere while the content remains stable and readable.</p>
        <button className="aurora-button" type="button" onClick={onStart} disabled={!onStart}>
          Explore
        </button>
      </article>
    </section>
  );
}
