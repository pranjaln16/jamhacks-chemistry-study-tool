import { useState} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';

import AddIcon from '@material-ui/icons/Add';
import Fab from '@material-ui/core/Fab';
import Button from '@material-ui/core/Button';
import Icon from '@material-ui/core/Icon';

const useStyles = makeStyles((theme) => ({
    root: {
      width: '100%',
      maxWidth: 360,
      backgroundColor: theme.palette.background.paper,
    },
  }));

    
const OurList = () => {
    const answerKey = [ ["H", "O", "O"],["Cl", "Na"]];
    
    const [elementsSelected, setElementsSelected] = useState([]);
    const [message, setMessage] = useState("")
    const [compound, setCompound] = useState("")
    const [correctness, setCorrectness] = useState();

    const hydrogen = ["hydrogen", "H", 1, 1, "gas", "hydride", 2] 
    const helium = ["helium", "He", 1, 8, "gas", null] 
    const lithium = ["lithium", "Li", 2, 1, "solid", null, 8]
    const beryllium = ["beryllium", "Be", 2, 2, "solid", null, 5]
    const boron = ["boron", "B", 2, 3, "solid", null, 1]
    const carbon = ["carbon", "C", 2, 4, "solid", "carbide", 3]
    const nitrogen = ["nitrogen", "N", 2, 5, "gas", "nitride"] 
    const oxygen = ["oxygen", "O", 2, 6, "gas", "oxide"] 
    const fluorine = ["fluorine", "F", 2, 7, "gas", "fluoride", 3] 
    const neon = ["neon","Ne", 2, 8, "gas", null]
    const sodium = ["sodium", "Na", 3, 1, "solid", null, 9]
    const magnesium = ["magnesium","Mg", 3, 2, "solid", null, 6]
    const aluminum = ["aluminum", "Al", 3, 3, "solid", null, 4]
    const silicon = ["silicon", "Si", 3, 4, "solid", null, 0]
    const phosphorous = ["phosphorous", "P", 3, 5, "solid", "phosphide", 0]
    const sulfur = ["sulfur", "S", 3, 6, "solid", "sulfide", 0]
    const chlorine = ["chlorine", "Cl", 3, 7, "gas", "chloride", 4] 
    const argon = ["argon", "Ar", 3, 8, "gas", null]
    const potassium = ["potassium", "K", 4, 1, "solid", null, 10]
    const calcium = ["calcium", "Ca", 4, 2, "solid", null, 7]
    const bromine = ["bromine", "Br", 4, 7, "liquid", "bromide", 2]
    const iodine = ["iodine", "I", 5, 7, "solid", "iodide", 1] 
    const nitrate = ["nitrate","NO3", -1]
    const chloride= ["chloride","Cl", -1]
    const sulfate = ["sulfate","SO4", -2]
    const acetate = ["acetate","C2H3O2", -1]
    const sodium_ion = ["sodium ion","Na", 1]
    const potassium_ion = ["potassium ion","K", 1]
    const ammonium = ["ammonium", "NH4", 1]
    const carbonate = ["carbonate", "CO3", -2]
    const phosphate = ["phosphate","PO4", -3]
    const hydroxide = ["hydroxide","OH", -1]
    const sulfide = ["sulfide","S", -2]
    const lead_ion = ["lead ion","Pb", 2]
    const copper_ion = ["copper ion","Cu", 1]
    const silver_ion = ["silver ion","Ag", 1]
    const mercury_ion = ["mercury ion","Hg", 2]
    const calcium_ion = ["calcium ion","Ca", 2]
    const strontium_ion = ["strontium ion","Sr", 2]
    const barium_ion = ["barium ion","Ba", 2]

    const menuItems = [hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon, sodium, magnesium, aluminum, silicon, phosphorous ,sulfur, chlorine, argon, potassium, calcium, bromine, iodine, nitrate, chloride, sulfate, acetate, sodium_ion, potassium_ion, ammonium, carbonate, phosphate, hydroxide, sulfide,lead_ion,copper_ion,silver_ion,mercury_ion,calcium_ion,strontium_ion,barium_ion]

    const ELEMENTS = [hydrogen, helium, lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon, sodium, magnesium, aluminum, silicon, phosphorous, sulfur, chlorine, argon, potassium, calcium]

    const HOFBRINCL = [hydrogen, oxygen, fluorine, bromine, iodine, nitrogen, chlorine]

    const IONS = [nitrate, chloride, sulfate, acetate, sodium_ion, potassium_ion, ammonium, carbonate, phosphate, hydroxide, sulfide]

    const metal_ions = [lead_ion , silver_ion, mercury_ion, calcium_ion, strontium_ion, barium_ion]
 
    const all_ions = metal_ions + IONS




    function handleClick(itemInfo){
        const itemsProposedList = [...elementsSelected, itemInfo[1]]
        // check if there's only two unique elements
        const uniqueItemsProposed = new Set(itemsProposedList)

        if (uniqueItemsProposed.size === 3) {
            setMessage("Only 2 unique items can be selected!")
        }
        // if:
        // check if the unique set is only two elements, if so then 
        // useState of message: set it cannot be two 
        else {
            // confirmed that there are 2 unique elements

        
        setElementsSelected([...elementsSelected, itemInfo[1]]);
    
            // check if elements Selected has only 1 distinct element -> append the index 0
            // else if element has 2 distinct element -> append the index 5

            let elementName = ''; 
            if (new Set([...elementsSelected, itemInfo[1]]).size === 1) {
                elementName = itemInfo[0];
            } else {
                if (itemInfo[5]){
                    elementName = itemInfo[5];
                } else {
                    elementName = itemInfo[0]
                }
            }

            setCompound(compound + " " + elementName );
        console.log(elementsSelected);
        }
    }

    function checkAnswer(items){

        // https://stackoverflow.com/questions/7837456/how-to-compare-arrays-in-javascript
        const array1 = items;

        let foundYet = false;
        answerKey.forEach(answer => {
            

            if (foundYet) {
                return;
            }

            const array2 = answer;
            const array2Sorted = array2.slice().sort();

            foundYet = JSON.stringify(items) === JSON.stringify(array2Sorted);

            setCorrectness(foundYet ? 'yes' : 'no');


        })
    }
    
    return (
        <>
        
        <div className='sidenav'>

        <List component="nav">

        {menuItems.map((item, index) => (<ListItem button key={index} onClick={()=>handleClick(item)} 
        
        
        className='list'>
            
            <ListItemIcon>
            <AddIcon />
          </ListItemIcon>

            <ListItemText primary={item[0]} />
            
            </ListItem>
      ))}


      </List>
        </div>

        <div className='main'>


            <h2>{message}</h2>
    
    <h1>  {correctness ==='yes' && "Correct!"} </h1>
    <h1>  {correctness ==='no' && "Try again"} </h1>
    <div className='circles'>


        {elementsSelected.map((element, currIndex) => (
            <div className='element-circle'>
        <Fab key={currIndex} color="primary" >
            {element}
        </Fab>
        </div>
      ))}


    </div>



    <h3>{compound}</h3>
    <Button
        variant="contained"
        color="secondary"
        className='submit'
        startIcon={<Icon>send</Icon>}
        onClick={()=>checkAnswer(elementsSelected)}
      >
        Check Answer
      </Button>
        </div>





    

    </>);
}
 


export default OurList;