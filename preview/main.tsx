import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { AuroraHero } from '../skills/aurora-ui/example';
import { SwissEditorialExample } from '../skills/swiss-editorial/example';
import './preview.css';

function Preview() {
  const initialStyle = new URLSearchParams(window.location.search).get('style') === 'swiss-editorial' ? 'swiss-editorial' : 'aurora-ui';
  const [style, setStyle] = useState<'aurora-ui' | 'swiss-editorial'>(initialStyle);
  const [effects, setEffects] = useState<'full' | 'off'>('full');
  const changeStyle = (value: 'aurora-ui' | 'swiss-editorial') => {
    setStyle(value);
    const url = new URL(window.location.href);
    if (value === 'aurora-ui') url.searchParams.delete('style');
    else url.searchParams.set('style', value);
    window.history.replaceState({}, '', url);
  };

  return <>
    <a className="preview-skip" href="#design-preview">Skip to design preview</a>
    <div className="preview-tools">
      <span>UI Morphism / Live React preview</span>
      <div className="preview-controls">
        <label>Style <select value={style} onChange={event => changeStyle(event.target.value as 'aurora-ui' | 'swiss-editorial')}><option value="aurora-ui">Aurora UI</option><option value="swiss-editorial">Swiss Editorial</option></select></label>
        {style === 'aurora-ui'
          ? <label>Effects <select value={effects} onChange={event => setEffects(event.target.value as 'full' | 'off')}><option value="full">Full</option><option value="off">Off</option></select></label>
          : <label>Theme <select defaultValue="system" onChange={event => {
              if (event.target.value === 'system') delete document.documentElement.dataset.theme;
              else document.documentElement.dataset.theme = event.target.value;
            }}><option value="system">System</option><option value="light">Light</option><option value="dark">Dark</option></select></label>}
      </div>
    </div>
    <main id="design-preview">{style === 'aurora-ui' ? <AuroraHero effects={effects} onStart={() => undefined} /> : <SwissEditorialExample />}</main>
  </>;
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><Preview /></React.StrictMode>);
