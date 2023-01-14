import React, {Component} from "react";
import {render} from "react-dom";
import {BrowserRouter as Router, Route, Link, Redirect, Routes, useRoutes} from "react-router-dom";
import HomePage from "./HomePage";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPage from "./RoomJoinPage";


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Router>
              <Routes>
                <Route path="/" element={<p>This is the home page</p>} />
                <Route path="/join/*" element={<RoomJoinPage />} />
                <Route path="/create" element={<CreateRoomPage />} />
              </Routes>
            </Router>
          );
    }
}

const AppDiv = document.getElementById("app");
render(<App/>, AppDiv);