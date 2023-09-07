import { 
    FormControl, 
    InputLabel, 
    Input, 
    Button, 
} 
from '@mui/material';

export default function RoomForm() {
    return <>
        <FormControl>
            <InputLabel htmlFor="my-input">Username</InputLabel>
            <Input id="my-input" aria-describedby="my-helper-text" />
        </FormControl>
    </>
}