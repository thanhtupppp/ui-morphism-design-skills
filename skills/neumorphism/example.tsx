import './example.css';
import { useState } from 'react';

export function NeumorphismToggle() {
  const [enabled, setEnabled] = useState(false);
  return <section className="neu-demo"><p>Air circulation: <strong>{enabled ? 'On' : 'Off'}</strong></p><button className="neu-control" type="button" aria-pressed={enabled} onClick={() => setEnabled(!enabled)}>{enabled ? 'Turn off' : 'Turn on'}</button></section>;
}
