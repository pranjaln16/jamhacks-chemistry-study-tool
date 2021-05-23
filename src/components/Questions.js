import { useState} from 'react';
import Button from '@material-ui/core/Button';

const Questions = () => {

    const [questionContent, setQuestionContent] = useState('hydrogen + oxygen');

    function handleClick(){
        console.log("it works!!")
        setQuestionContent("sodium + chlorine");
        console.log(questionContent);
    }

    return (<div className='questions'>
        <p>Chemhacks</p> <p>Question: {questionContent} = </p>
        <Button
        variant="contained"
        color= 'primary'
        className='submit'
        onClick={handleClick}
      >
        New Question!
      </Button>
    </div> );
}
 
export default Questions;