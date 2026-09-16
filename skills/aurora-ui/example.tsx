'use client';

import React, { useId, useState } from 'react';
import './example.css';

const modes = [
  { id: 'discover', number: '01', label: 'Discover', title: 'Find the strongest signal.', body: 'Map the problem, audience, and constraints before the visual system takes shape.', meta: 'Research · intent · context' },
  { id: 'compose', number: '02', label: 'Compose', title: 'Turn atmosphere into structure.', body: 'Use Aurora behind stable surfaces, then let type, spacing, and hierarchy carry meaning.', meta: 'Tokens · layout · content' },
  { id: 'verify', number: '03', label: 'Verify', title: 'Keep the experience resilient.', body: 'Remove glow, motion, and transparency to confirm that every action and state still works.', meta: 'Contrast · fallback · performance' },
] as const;

export function AuroraHero({ effects = 'full', onStart }: { effects?: 'full' | 'off'; onStart?: () => void }) {
  const id = useId();
  const [activeMode, setActiveMode] = useState<(typeof modes)[number]['id']>('discover');
  const [launched, setLaunched] = useState(false);
  const selected = modes.find(mode => mode.id === activeMode) ?? modes[0];
  const start = () => {
    setLaunched(true);
    onStart?.();
  };

  return (
    <section className="aurora-demo" data-effects={effects} aria-labelledby={`${id}-title`}>
      <div className="aurora-shell">
        <header className="aurora-nav">
          <a className="aurora-brand" href={`#${id}-title`} aria-label="Luma home">
            <span className="aurora-brand-mark" aria-hidden="true" />
            Luma
          </a>
          <nav aria-label="Aurora preview">
            <a href={`#${id}-capabilities`}>Capabilities</a>
            <a href={`#${id}-workflow`}>Workflow</a>
          </nav>
          <p className="aurora-status"><span aria-hidden="true" /> System online</p>
        </header>

        <div className="aurora-hero">
          <div className="aurora-copy">
            <p className="aurora-eyebrow"><span>Independent design system</span><span>Edition 01</span></p>
            <h1 id={`${id}-title`}>Ideas become<br /><span>visible signals.</span></h1>
            <p className="aurora-intro">A calm interface for ambitious work. Aurora creates atmosphere around the content while every surface, state, and action stays clear.</p>
            <div className="aurora-actions">
              <button className="aurora-button" type="button" onClick={start} disabled={!onStart}>Explore the system <span aria-hidden="true">↗</span></button>
              <a className="aurora-link" href={`#${id}-workflow`}>See the workflow <span aria-hidden="true">↓</span></a>
            </div>
            <p className="aurora-live" role="status">{launched ? 'System exploration started. Choose a workflow phase below.' : 'Ready for exploration.'}</p>
          </div>

          <aside className="aurora-signal" aria-label="Live Aurora signal">
            <div className="aurora-orbit" aria-hidden="true"><span /><span /><span /></div>
            <div className="aurora-signal-top"><span>Live signal</span><span>14:32:08</span></div>
            <strong>98.6</strong>
            <p>Clarity index</p>
            <div className="aurora-wave" aria-hidden="true">{[24, 44, 30, 62, 38, 76, 48, 68, 34, 54, 28, 46].map((height, index) => <i key={index} style={{ height }} />)}</div>
            <div className="aurora-signal-bottom"><span><b /> Stable</span><span>+12.4%</span></div>
          </aside>
        </div>

        <section className="aurora-capabilities" id={`${id}-capabilities`} aria-labelledby={`${id}-capabilities-title`}>
          <div className="aurora-section-heading">
            <div><p>What the system protects</p><h2 id={`${id}-capabilities-title`}>Atmosphere with discipline.</h2></div>
            <p>Glow supports the experience. Structure makes it work.</p>
          </div>
          <div className="aurora-card-grid">
            <article className="aurora-card"><span className="aurora-card-index">01</span><div className="aurora-card-icon" aria-hidden="true">✦</div><h3>Stable content</h3><p>Opaque reading surfaces keep text reliable across every backdrop and device.</p></article>
            <article className="aurora-card aurora-card-featured"><span className="aurora-card-index">02</span><div className="aurora-card-icon" aria-hidden="true">◌</div><h3>Bounded effects</h3><p>Ambient fields stay behind the interface and simplify before performance suffers.</p></article>
            <article className="aurora-card"><span className="aurora-card-index">03</span><div className="aurora-card-icon" aria-hidden="true">⌁</div><h3>Explicit state</h3><p>Focus, selection, loading, and status never depend on color or glow alone.</p></article>
          </div>
        </section>

        <section className="aurora-workflow" id={`${id}-workflow`} aria-labelledby={`${id}-workflow-title`}>
          <div className="aurora-workflow-intro"><p>Method / 03 phases</p><h2 id={`${id}-workflow-title`}>From intent to interface.</h2></div>
          <div className="aurora-mode-picker" role="group" aria-label="Choose workflow phase">
            {modes.map(mode => <button key={mode.id} type="button" aria-pressed={activeMode === mode.id} onClick={() => setActiveMode(mode.id)}><span>{mode.number}</span>{mode.label}</button>)}
          </div>
          <article className="aurora-mode-panel" aria-live="polite">
            <p>{selected.number} / {selected.label}</p>
            <h3>{selected.title}</h3>
            <p>{selected.body}</p>
            <span>{selected.meta}</span>
          </article>
        </section>

        <footer className="aurora-footer"><strong>Luma / Aurora UI</strong><p>Atmosphere follows meaning.</p><span>Accessible by design · 2026</span></footer>
      </div>
    </section>
  );
}

// Verification: rendered directly by preview/; interactions and responsive checks live in tests/aurora-ui.spec.ts.
// Fallback: effects="off" removes Aurora fields while content, hierarchy, states, and controls remain unchanged.
