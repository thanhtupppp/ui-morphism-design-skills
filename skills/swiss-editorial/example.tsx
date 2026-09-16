'use client';

import React, { useId, useState } from 'react';
import './example.css';

const stories = [
  { id: '01', category: 'Design', title: 'Less noise. More meaning.', summary: 'On making room for the things that deserve our attention.', body: 'A clear interface starts with a clear decision: what matters here? Remove the competing signals, give the content room to breathe, and let the next action speak for itself.' },
  { id: '02', category: 'Culture', title: 'The city is a type specimen.', summary: 'A field guide to the letters we walk past every day.', body: 'Shopfronts, station signs, and handwritten notices tell a living story. Their type carries the pace of a neighbourhood, from careful permanence to a note made in a hurry.' },
  { id: '03', category: 'Design', title: 'A grid is a starting point.', summary: 'Structure that makes space for an unexpected idea.', body: 'A useful grid connects things without making them identical. Start with the reading order, align what belongs together, and break the pattern only when the content gives you a reason.' },
];
const categories = ['All', 'Design', 'Culture'];

export function SwissEditorialExample() {
  const id = useId();
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState('All');
  const [saved, setSaved] = useState<string[]>([]);
  const [expanded, setExpanded] = useState<string[]>([]);
  const visible = stories.filter(story =>
    (category === 'All' || story.category === category) &&
    `${story.title} ${story.summary}`.toLocaleLowerCase().includes(query.trim().toLocaleLowerCase()),
  );
  const reset = () => { setQuery(''); setCategory('All'); };
  const toggle = (values: string[], key: string) => values.includes(key) ? values.filter(value => value !== key) : [...values, key];

  return (
    <section className="swiss-demo" aria-labelledby={`${id}-title`}>
      <div className="swiss-shell">
        <header className="swiss-masthead">
          <a className="swiss-brand" href={`#${id}-title`}>FORM<span aria-hidden="true"> / </span>FIELD</a>
          <p className="swiss-meta">An independent journal<br />Design, culture & everyday life</p>
          <nav className="swiss-nav" aria-label="Journal">
            <a href={`#${id}-index`}>The index</a>
            <a href={`#${id}-about`}>About</a>
          </nav>
        </header>

        <div className="swiss-hero">
          <div>
            <p className="swiss-kicker">Volume 01 / The clarity issue</p>
            <h1 id={`${id}-title`}>A little less.<br /><span>A lot more.</span></h1>
            <p className="swiss-intro">Notes on thoughtful design. Stories about the space between what we make and how we live.</p>
          </div>
          <div className="swiss-cover" aria-hidden="true"><span>F/F</span><strong>01</strong><span>Clarity is a practice.</span></div>
        </div>

        <section className="swiss-index" aria-labelledby={`${id}-index`}>
          <div className="swiss-index-heading">
            <h2 id={`${id}-index`}>The index<span aria-hidden="true"> ↘</span></h2>
            <p role="status">{visible.length} {visible.length === 1 ? 'story' : 'stories'} / {saved.length} saved</p>
          </div>
          <div className="swiss-toolbar">
            <div className="swiss-filters" role="group" aria-label="Filter by category">
              {categories.map(item => <button key={item} className="swiss-button" type="button" aria-pressed={category === item} onClick={() => setCategory(item)}>{category === item && <span aria-hidden="true">✓ </span>}{item}</button>)}
            </div>
            <div className="swiss-field">
              <label htmlFor={`${id}-search`}>Search the journal</label>
              <input id={`${id}-search`} type="search" value={query} onChange={event => setQuery(event.target.value)} placeholder="A title, an idea…" />
            </div>
          </div>
          <div className="swiss-stories">
            {visible.map(story => <article key={story.id} className="swiss-story" aria-labelledby={`${id}-${story.id}-title`}>
              <p className="swiss-story-meta"><span>{story.id} / {story.category}</span><span>Field notes</span></p>
              <h3 id={`${id}-${story.id}-title`}>{story.title}</h3>
              <p className="swiss-summary">{story.summary}</p>
              <div className="swiss-actions">
                <button className="swiss-read" type="button" aria-expanded={expanded.includes(story.id)} aria-controls={`${id}-${story.id}-body`} onClick={() => setExpanded(previous => toggle(previous, story.id))}>{expanded.includes(story.id) ? 'Close story −' : 'Read story ↗'}<span className="swiss-sr-only">: {story.title}</span></button>
                <button className="swiss-button" type="button" aria-pressed={saved.includes(story.id)} onClick={() => setSaved(previous => toggle(previous, story.id))}>{saved.includes(story.id) ? '✓ Saved' : '+ Save'}<span className="swiss-sr-only">: {story.title}</span></button>
              </div>
              <p className="swiss-body" id={`${id}-${story.id}-body`} hidden={!expanded.includes(story.id)}>{story.body}</p>
            </article>)}
          </div>
          {visible.length === 0 && <div className="swiss-empty"><h3>No stories found</h3><p>Try another title or browse the full index.</p><button className="swiss-button" type="button" onClick={reset}>Reset filters</button></div>}
        </section>
        <footer className="swiss-footer" id={`${id}-about`}>
          <strong>Good things need room.</strong>
          <p>FORM / FIELD is a fictional journal demonstrating Swiss Editorial. Bookmarks stay in this session.</p>
          <span className="swiss-meta">End of volume / 01</span>
        </footer>
      </div>
    </section>
  );
}

// Verification: rendered directly by preview/; browser interactions and responsive checks in tests/swiss-editorial.spec.ts.
// Fallback: system font, opaque surfaces, ordinary document flow; no decorative effect carries state.
