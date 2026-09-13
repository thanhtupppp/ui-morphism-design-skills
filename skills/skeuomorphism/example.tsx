import './example.css';

export function SkeuomorphismControl() {
  return (
    <section className="skeuo-demo" aria-labelledby="skeuo-title">
      {/* Responsive intent: the stylesheet reduces panel padding at compact widths. */}
      <div className="skeuo-panel">
        <h2 id="skeuo-title">Studio Console</h2>
        <p>Physical material cues support the control, but labels remain explicit.</p>
        <button className="skeuo-button" type="button" data-state="ready">
          Start recording
        </button>
      </div>
    </section>
  );
}
