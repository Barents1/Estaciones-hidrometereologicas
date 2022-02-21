import { SideBarMenuItem, SideBarMenuCard } from "../types/types.d";
import {useState} from "react";
import {classNames} from "../util/classes";
import {VscMenu} from "react-icons/vsc"
import SideBarMenuCardView from "./SideBarMenuCardView"
import SideBarMenuItemView from "./SideBarMenuItemView"
import '../Styles/SideBarMenu.scss'
import '../Styles/App.scss'
import {BrowserRouter as Router,Route,Link} from "react-router-dom";
interface SideBarMenuProps{

    items:SideBarMenuItem[];
    card:SideBarMenuCard;
}

export function SideBarMenu({items,card}:SideBarMenuProps){

      const[isOpen, setIsOpen] = useState<boolean>(false);


      function handleClick(){
        setIsOpen(!isOpen);
      }

    return (


    <div className={classNames("SideBarMenu", isOpen ? "expanded" : "collapsed")}
    >
      
       <div className="menuButton">
         <button className="hamburgerIcon" onClick={handleClick}>
            <VscMenu/>
        </button>  
         
       </div>  
       <SideBarMenuCardView card={card} isOpen={isOpen}/>
       {items.map((item) => (

       <SideBarMenuItemView key={item.id} item={item} isOpen={isOpen} />
       ))}
       
     </div>

    );
}