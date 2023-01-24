import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { TextField, Button, Grid, Typography } from "@mui/material";  
import { Link , useNavigate} from 'react-router-dom';


export default function Room (){
    const navigate = useNavigate();

    const[VoteToSkip, setVoteToSkip] = useState(2)
    const[GuestCanPause, setGuestCanPause] =  useState(false)
    const[isHost, setIsHost] = useState(false)
    
    const{roomCode} = useParams()
    

    fetch(`/api/get-room?code=${roomCode}`)
    .then((response) => response.json())
    .then((data) => {
            
        setVoteToSkip(data.Votes_To_Skip)
        setGuestCanPause(data.Guest_Can_Pause)
        setIsHost(data.Is_Host)
            
    });

    const LeaveButtonPressed = () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        };

        fetch(`/api/leave-room`, requestOptions)
        .then(_response => {
            props.clearRoomCodeCallback(); // clears roomCode state in HomePage
            navigate("/");
        });
    };
    
    return (
        <Grid container spacing={1}>
            
            <Grid item xs={12} align='center'>
                <Typography variant="h4" component='h4'>
                    Code: {roomCode}
                </Typography>
            </Grid>

            <Grid item xs={12} align='center'>
                <Typography variant="h4" component='h4'>
                    Votes: {VoteToSkip}
                </Typography>
            </Grid>

            <Grid item xs={12} align='center'>
                <Typography variant="h4" component='h4'>
                    Guest Can Pause: {GuestCanPause}
                </Typography>
            </Grid>

            <Grid item xs={12} align='center'>
                <Typography variant="h4" component='h4'>
                    Host: {isHost}
                </Typography>
            </Grid>

            <Grid item xs={12} align='center'>
                <Button variant='contained' color ='secondary' to='/' onClick={LeaveButtonPressed}>
                    Leave Room
                </Button>
            </Grid>

        </Grid>
        /*
        <div>
            <h3>{roomCode}</h3>
            <p>Votes: {VoteToSkip}</p>
            <p>Guest Can Pause: {String(GuestCanPause)}</p>
            <p>Host: {String(isHost)}</p>
        </div>
        */
    );

}