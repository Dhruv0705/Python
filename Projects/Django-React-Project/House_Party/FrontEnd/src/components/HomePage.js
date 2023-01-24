import React, {Component, useState} from "react";
import {BrowserRouter as Router, Route, Link, Redirect, Routes, useRoutes, Navigate} from "react-router-dom";
import { Grid, Button, ButtonGroup, Typography } from "@mui/material"
import CreateRoomPage from "./CreateRoomPage";
import JoinRoomPage from "./JoinRoomPage";
import Room from './Room';


export default function HomePage (props) {

    const {roomCode} = useState(null);
    
    async componentDidMount() {
        const response = await fetch("/api/user-in-room");
        const data = await response.json();
        this.setState({
            roomCode:data.code
        });
    }

    const clearRoomCode = () => {
        setState({roomCode: null})
    }
    
    renderHomePage(){
        if(this.state.roomCode) {
            return(
              <Navigate to={`/room/${this.state.roomCode}`} replace={true} />
            );
        }
        else {
            return (
                <Grid container spacing={3}>

                    <Grid item xs={12} align="center">
                        <Typography variant="h3" compact="h3">
                            Music Sync
                        </Typography>
                    </Grid>

                    <Grid item xs={12} align="center">
                        <ButtonGroup disableElevation variant="contained" color="primary">
                            <Button color="primary" to="/join" component={Link}>
                                Join a Room
                            </Button>
                            <Button color="secondary" to="/create" component={Link}>
                                Create a Room
                            </Button>
                        </ButtonGroup>
                    </Grid>

                </Grid>
            );
        };
    }
    
    render() {
        return (
            <Router>
                <Routes>
                    <Route exact path="/" element={this.renderHomePage()} />
                    <Route path="/join/*" element={<JoinRoomPage />} />
                    <Route path="/create/" element={<CreateRoomPage />} />
                    <Route exact path="/room/:roomCode/" element={<Room />} render={({ match }) => <Room id={match.params.roomCode} />} />
                </Routes>
            </Router>
        );
    };
}
