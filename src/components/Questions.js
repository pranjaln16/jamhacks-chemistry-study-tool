import { useState} from 'react';

const Questions = () => {

    const [questionContent, setQuestionContent] = useState('hydrogen + oxygen');

    function handleClick(){
        console.log("it works!!")
        setQuestionContent("sodium + chlorine");
        console.log(questionContent);
    }

    return (<div className='questions'>
        <p>Question: {questionContent} = </p>
        <button onClick={handleClick}>New Question!</button>
    </div> );
}
 
export default Questions;