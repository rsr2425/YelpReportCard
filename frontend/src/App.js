import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      reviewList: [],
      modal: false,
      activeItem: {
        title: "",
        review_text: "",
      },
    };
  }
  
  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/reviews/")
      .then((res) => this.setState({ reviewList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axios
        .put(`/api/reviews/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("/api/reviews/", item)
      .then((res) => this.refreshList());
  };

  handleDelete = (item) => {
    axios
      .delete(`/api/reviews/${item.id}/`)
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = { title: "", review_text: ""};

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };


  renderItems = () => {
    const newItems = this.state.reviewList

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className="review-title mr-5"
          title={item.review_text}
        >
          {item.title}
        </span>
        <table class="table table-light">
          <tbody>
            <td>{item.food_grade}</td>
            <td>{item.service_grade}</td>
            <td>{item.vibe_grade}</td>
          </tbody>
        </table>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
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
        <h1 className="text-black text-uppercase text-center my-4">Yelp Report Card</h1>
        <div className="row">
          <div className="col-md-9 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add Review
                </button>
              </div>
              <li
                key="header"
                className="list-group-item d-flex justify-content-between align-items-center"
              >
                <span
                  className="review-title mr-4 font-weight-bold"
                  title="review_text"
                >
                  Review Title
                </span>
                <table class="table table-light font-weight-bold">
                  <tbody>
                    <td>Food Grade</td>
                    <td>Service Grade</td>
                    <td>Vibe Grade</td>
                  </tbody>
                </table>
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
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default App;
