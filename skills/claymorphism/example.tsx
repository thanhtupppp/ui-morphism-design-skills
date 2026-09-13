import './example.css';

export function ClaymorphismWelcome() {
  return (
    <section className="clay-demo" aria-labelledby="clay-demo-title">
      <article className="clay-card" data-layout="responsive" data-state="default">
        <h2 id="clay-demo-title">Welcome back</h2>
        <p>Use soft volume for the object, but keep content and focus states crisp.</p>
        <button className="clay-button" type="button" data-state="default">
          Continue learning
        </button>
      </article>
    </section>
  );
}
