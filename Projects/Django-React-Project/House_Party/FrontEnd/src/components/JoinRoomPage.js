import React, {Component, useState} from "react";
import { TextField, Button, Grid, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import {useNavigate} from 'react-router-dom';

export default function RoomJoinPage (props){
    const navigate = useNavigate();

    const[roomCode, setRoomCode] = useState('');
    const[Error, setError] = useState('');


    const HandleTextFieldChange = event => {
        setRoomCode(event.target.value);
    };

    const RoomJoinButtonPressed = () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                code: roomCode,
        }),
        };
        fetch("/api/join-room", requestOptions)
            .then((response) => {
            if (response.ok) {
                navigate(`/room/${roomCode}`)
            } 
            else {
                setError("Room not found.");
            }
        })
            .catch((error) => {
                console.log(error);
        });
    };
    

    return (
        <Grid container spacing={1}>
            
            <Grid item xs={12} align="center">
                <Typography variant="h4" component="h4">
                    Join a Room
                </Typography>
            </Grid>

            <Grid item xs={12} align="center">
                <TextField
                    error={Error}
                    label="Code"
                    placeholder="Enter a Room Code"
                    value={roomCode}
                    helperText={Error}
                    variant="outlined"
                    onChange={HandleTextFieldChange}/>
            </Grid>

            <Grid item xs={12} align="center">
                <Button
                    variant="contained"
                    color="primary"
                    onClick={RoomJoinButtonPressed}>
                    Enter Room
                </Button>
            </Grid>
            
            <Grid item xs={12} align="center">
                <Button variant="contained" color="secondary" to="/" component={Link}>
                    Back
                </Button>
            </Grid>
        </Grid>
    );
}