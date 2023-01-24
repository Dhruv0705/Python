import React, { useState , useEffect} from "react";
import { useParams , useNavigate } from "react-router-dom";
import { TextField, Button, Grid, Typography } from "@mui/material";  
import CreateRoomPage from "./CreateRoomPage";  



export default function Room () {
    const navigate = useNavigate();

    const[VotesToSkip, setVotesToSkip] = useState(2)
    const[GuestCanPause, setGuestCanPause] =  useState(false)
    const[IsHost, setIsHost] = useState(false)
    const[ShowSettings, setShowSettings] = useState(false)
    
    const{roomCode} = useParams()
    
    useEffect ( () => {
        fetch(`/api/get-room?code=${roomCode}`)
            .then(response => {
                if (!response.ok) {
                    clearRoomCodeCallback(); // clears roomCode state in HomePage
                    navigate("/");
                } else {
                    return response.json();
                }
            })
            .then(data => {
                
                    setVotesToSkip (data.Votes_To_Skip);
                    setGuestCanPause (data.Guest_Can_Pause);
                    setIsHost (data.Is_Host);
                
            });
    }, []);
    
    const LeaveButtonPressed = () => {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        };
        fetch(`/api/leave-room`, requestOptions)
            .then(_response => {
                clearRoomCodeCallback(); // clears roomCode state in HomePage
                navigate("/");
            }
        );
    }

    const updateShowSettings = (value) => {
        setShowSettings(value);
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
                    Votes: {VotesToSkip}
                </Typography>
            </Grid>

            <Grid item xs={12} align='center'>
                <Typography variant="h4" component='h4'>
                    Guest Can Pause: {GuestCanPause}
                </Typography>
            </Grid>

            <Grid item xs={12} align='center'>
                <Typography variant="h4" component='h4'>
                    Host: {IsHost}
                </Typography>
            </Grid>

            <Grid item xs={12} align='center'>
                <Button variant='contained' color ='secondary' onClick={LeaveButtonPressed}>
                    Leave Room
                </Button>
            </Grid>

        </Grid>
        /*
        <div>
            <h3>{roomCode}</h3>
            <p>Votes: {VoteToSkip}</p>
            <p>Guest Can Pause: {String(GuestCanPause)}</p>
            <p>Host: {String(IsHost)}</p>
        </div>
        */
    );

}