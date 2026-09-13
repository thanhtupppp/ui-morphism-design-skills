import './example.css';
import { useState } from 'react';

export function NeumorphismToggle() {
  const [enabled, setEnabled] = useState(false);
  return (
    <section className="neu-demo" aria-label="Air circulation control">
      {/* Responsive intent: the CSS stacks the control to full width on compact screens. */}
      <p>Air circulation: <strong>{enabled ? 'On' : 'Off'}</strong></p>
      <button
        className="neu-control"
        type="button"
        aria-pressed={enabled}
        data-state={enabled ? 'on' : 'off'}
        onClick={() => setEnabled(!enabled)}
      >
        {enabled ? 'Turn off' : 'Turn on'}
      </button>
    </section>
  );
}
