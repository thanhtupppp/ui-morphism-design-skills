import './example.css';

export function LiquidGlassToolbar() {
  return (
    <nav className="liquid-toolbar" aria-label="Quick actions">
      {/* Responsive intent: the toolbar may wrap or stack without changing action order. */}
      <button className="liquid-button" type="button" data-state="ready">Home</button>
      <button className="liquid-button" type="button" data-state="ready">Search</button>
      <button className="liquid-button" type="button" data-state="ready">Profile</button>
    </nav>
  );
}
