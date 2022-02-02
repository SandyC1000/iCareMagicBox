'use strict';

function Homepage() {

  return (
    <div>
      <h1>Welcome!</h1>
      <p><a href="/packages">Go to the Packages Page</a></p>
      <img src="/static/img/Cloud1.png"/>

      <p><a href="/about">Go the the About Page</a></p>
    </div>
  );
}

ReactDOM.render(<Homepage />, document.querySelector('#app'));