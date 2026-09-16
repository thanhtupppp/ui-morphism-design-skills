import React from 'react';
import { createRoot } from 'react-dom/client';
import { SwissEditorialExample } from '../skills/swiss-editorial/example';
import './preview.css';

function Preview() {
  return <>
    <a className="preview-skip" href="#journal">Skip to journal</a>
    <div className="preview-tools">
      <span>UI Morphism / Swiss Editorial</span>
      <label>Theme <select defaultValue="system" onChange={event => {
        if (event.target.value === 'system') delete document.documentElement.dataset.theme;
        else document.documentElement.dataset.theme = event.target.value;
      }}><option value="system">System</option><option value="light">Light</option><option value="dark">Dark</option></select></label>
    </div>
    <main id="journal"><SwissEditorialExample /></main>
  </>;
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><Preview /></React.StrictMode>);
