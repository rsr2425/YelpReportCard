import logo from './logo.svg';
import './App.css';
import React, { Component } from "react";

const reviewItems = [
  {
    id: 1,
    title: "Test Review",
    review_text: "This was a tasty restuarant.",
    food_grade: "A",
    service_grade: "A",
    vibe_grade: "A",
  },
  {
    id: 2,
    title: "A bad Review",
    review_text: "This was an aweful restuarant.",
    food_grade: "D",
    service_grade: "B",
    vibe_grade: "F",
  },
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      reviewList: reviewItems,
    };
  }

  renderItems = () => {
    const newItems = this.state.reviewList

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className="review-title mr-2"
          title={item.review_text}
        >
          {item.title}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                >
                  Add Review
                </button>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;

/* function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App; */
