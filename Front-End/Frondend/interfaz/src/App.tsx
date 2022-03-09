import {useState} from "react";
import { SideBarMenu } from './components/SideBarMenu';
import { SideBarMenuItem, SideBarMenuCard } from "./types/types.d";
import {FcKindle,FcCalendar,FcUpload} from "react-icons/fc";
import prorfileImage from './images/Apolo.jpg'
import {BrowserRouter, Route,NavLink, Routes} from 'react-router-dom';
import {V1073161h} from './tablas_db/V1073161h';
import { Home } from "./Home";
import {V29311hval} from './tablas_db/V29311hval';

import {V29311h} from './tablas_db/V29311h';
import './Styles/App.scss'
import Select from 'react-select';
function App () {


  

    const items: SideBarMenuItem [] = [
        {

            id:"1",
            label:"Ingreso de datos",
            icon:FcKindle,
            url:"Home"
        },
        {

          id:"2",
          label:"Generar Reportes",
          icon:FcCalendar,
          url:"/"
      },
      {

        id:"3",
        label:"Exportar Datos",
        icon:FcUpload,
        url:"/"
    },

          ];
    const card: SideBarMenuCard  =
        {
                id:"card01",
                dysplayName:"Juan Apolo",
                title:"Programador",
                photoUrl:prorfileImage,
                url:"/",
        };
   
  return (


    <div >


     

<SideBarMenu items={items} card={card} />

  
<BrowserRouter>
  <Routes>
  
      <Route path='/home' element={<Home/>}/>
      <Route path='/t1073161h' element={<V1073161h/>}/>
      
      <Route path='/V29311hval' element={<V29311hval/>}/>
      <Route path='/V29311h' element={<V29311h/>}/>
  </Routes>
  </BrowserRouter>

  </div >


  );
}

export default App;
