import './App.css';
import Questions from './components/Questions';
import OurList from './components/List';

function App() {
  return (
    <div className="App">
      <Questions />
      <div className='content'>
          <OurList />
      </div>

    </div>
  );
}

export default App;
