import React, {Component} from "react";
import {render} from "react-dom";
import {BrowserRouter as Router, Route, Link, Redirect, Routes, useRoutes} from "react-router-dom";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPage from "./RoomJoinPage";
import Room from './Room';


export default function HomePage (props){

    return (
        <Router>
            <Routes>
                <Route path="/" element={<p>This is the home page</p>} />
                <Route path="/join" element={<RoomJoinPage/>} />
                <Route path="/create" element={<CreateRoomPage/>} />
                <Route path="/room/:roomCode" element={<Room/>}/>
            </Routes>
        </Router>
    );
}
