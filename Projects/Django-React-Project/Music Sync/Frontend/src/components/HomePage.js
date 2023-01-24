import React, {Component, useState, useEffect} from "react";
import {BrowserRouter as Router, Route, Link, Redirect, Routes, useRoutes, Navigate} from "react-router-dom";
import { Grid, Button, ButtonGroup, Typography } from "@mui/material"
import CreateRoomPage from "./CreateRoomPage";
import JoinRoomPage from "./JoinRoomPage";
import Room from './Room';


export default function HomePage (props) {

    const [roomCode, setRoomCode] = useState(null);
    
    useEffect(() => {
        async function fetchData() {
            const response = await fetch("/api/user-in-room");
            const data = await response.json();
            setRoomCode(data.code);
        }
        fetchData();
    }, []);

    const clearRoomCode = () => {
        setRoomCode(null);
    }
    
    const renderHomePage = () => {
        if(roomCode) {
            return(
                <Navigate to={`/room/${roomCode}`} replace={true} />
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
    
    return (
        <Router>
            <Routes>
                <Route exact path="/" element={renderHomePage()} />
                <Route path="/join/*" element={<JoinRoomPage />} />
                <Route path="/create/" element={<CreateRoomPage />} />
                
                <Route exact path="/room/:roomCode/" element={<Room />} render={({ match }) => <Room id={match.params.roomCode} />} />
            </Routes>
        </Router>
    );
}


/*<Route path='/room/:roomCode' element={<Room clearRoomCodeCallback={clearRoomCode} />} />*/
