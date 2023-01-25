import React, { useState, Component } from "react";
import { Link } from "react-router-dom";
import { Button, Grid, Typography, TextField, FormHelperText, FormControl, FormControlLabel, RadioGroup, Radio } from "@mui/material";
import {useNavigate} from 'react-router-dom';

export default function CreateRoomPage (props){
    const navigate = useNavigate();
    const {roomCode} = useState(null);

    const[DefaultVotes, setDefaultVotes] = useState(2);
    const[GuestCanPause, setGuestCanPause] = useState(true);
    const[VotesToSkip, setVotesToSkip] = useState(DefaultVotes);
    const[Update, setUpdate] = useState(false);
    const updateCallback = () => {};
    
    
    const HandleVotesChange = (event) => {
        setVotesToSkip(event.target.value);
    };
    
    const HandleGuestCanPauseChange = event => {
        setGuestCanPause(event.target.value === "true" ? true : false);
    };

    const HandleRoomButtonPressed = () => {
        const requestOptions = {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                Votes_To_Skip: VotesToSkip,
                Guest_Can_Pause: GuestCanPause,
            }),
        };
        fetch("/api/create-room", requestOptions)
            
            .then((response) => response.json())
            .then((data) => navigate('/room/'+ data.code)
        
        );
    };
    
    return (
        <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <Typography component="h4" variant="h4">Create A Room</Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl component="fieldset">
                    <FormHelperText>
                        <Typography component= "span" variant="body2" align="center">Guest Control of Playback State</Typography>
                    </FormHelperText>
                    <RadioGroup row defaultValue="true" onChange={HandleGuestCanPauseChange}>
                        <FormControlLabel 
                            value="true" 
                            label="Play/Pause"
                            labelPlacement="bottom"
                            control={<Radio color="primary"/>}
                        />
                        <FormControlLabel
                            value="false"
                            label="No Control"
                            labelPlacement="bottom"
                            control={<Radio color="secondary"/>}
                        />
                    </RadioGroup>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <FormControl>
                    <TextField 
                        required={true} 
                        type="number" 
                        onChange = {HandleVotesChange}
                        defaultValue = {DefaultVotes}
                        inputProps={{ min:1, style:{textAlign:"center"}, }} 
                    />
                    <FormHelperText>
                        <Typography component= "span" variant="body2" align="center">Votes Required To Skip Songs</Typography>
                    </FormHelperText>
                </FormControl>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="primary" variant="contained" onClick={HandleRoomButtonPressed}>Create A Room</Button>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="secondary" variant="contained" to="/" component={Link}>Back</Button>
            </Grid>
        </Grid>
    );
}