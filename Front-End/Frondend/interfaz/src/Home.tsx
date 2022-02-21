import React,{Component} from "react";
import './Styles/buscador.scss'
import Tablas from "./data/data.json"





interface IProps {

   

}
interface IState {

    searchTem:string,
  
  
}
export class Home extends Component<IProps,IState> {

    constructor(props: IProps){
        super(props);

        
        this.state={
            searchTem:"",
           
 
        }
    }


    set =(e:any)=>{
        this.setState({
            searchTem:e.target.value
            
        });
    }
    render(){
        const {
            searchTem,
           
        }=this.state;


        return(
           
            <div  className="Home">
                <h1>
               .
                </h1>
                <h3>
                   .
                    </h3>   
                    <h3>
                   .
                    </h3> 
                    <h3>
                  .
                    </h3> 
                    
                   
                <input   className="in" type="text" placeholder="Search..." onChange={this.set}/>    
            
              
  
                {Tablas.filter((val)=>{
                    if(searchTem==""){
                        return val
                    }else if(val.name.toLowerCase().includes(searchTem.toLowerCase())){
                        return val
                    }
                }
                ).map((val,key)=>{
                    return (
                    
                    <div key={key}>

                          <a className="a_buscador" href={val.name}>
                        
                        <p>
                        {val.name}
                        </p>
                       
                       
                        </a>   
                    </div>
                    );
                })}
                    
               
            </div>
           
        )
    }
}