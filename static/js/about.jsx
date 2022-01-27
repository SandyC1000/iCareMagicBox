'use strict';

function About() {

  return (
    <div>
      <h1>About us</h1>
      <p><a href="https://github.com/">Sandy</a></p>
      <p>Hello this is Sandy.</p>

      <p><a href="/">Go back to the Homepage</a></p>
    </div>
  );
}

ReactDOM.render(<About />, document.querySelector('#about'));