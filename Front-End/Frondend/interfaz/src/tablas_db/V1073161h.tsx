import React,{Component} from "react";
import {variables} from '../Variables';
import '../Styles/tablas.scss'

interface IProps {

}

interface IState {

    v1073161hs:any[],
    modalTitle:string,
    id_temp_int_baro: number,
    id_estacion: number,
    id_unidad_medida: number,
    id_usuario: number,
    fecha_toma: string,
    fecha_ingreso: string,
    valor: number,

    
    v1073161hsFilter:any[],
    id_temp_int_baroFilter: number,
    id_estacionFilter: number,
    id_unidad_medidaFilter: number,
    id_usuarioFilter: number,
    fecha_tomaFilter: string,
    fecha_ingresoFilter: string,
    valorFilter: number,

}

export class V1073161h extends Component<IProps,IState> {

    constructor(props: IProps){
        super(props);

        this.state={
            v1073161hs:[''],
            modalTitle:"",
            id_temp_int_baro:0,
            id_estacion:0,
            id_unidad_medida: 0,
            id_usuario: 0,
            fecha_toma:'',
            fecha_ingreso:'',
            valor: 0,

            v1073161hsFilter:[''],
            id_temp_int_baroFilter: 0,
            id_estacionFilter: 0,
            id_unidad_medidaFilter: 0,
            id_usuarioFilter: 0,
            fecha_tomaFilter: '',
            fecha_ingresoFilter: 'string',
            valorFilter:0,


            
 
        }
    }
    FilterFn(){
        
        var  id_temp_int_baroFilter=this.state.id_temp_int_baroFilter;
        var id_estacionFilter = this.state.id_estacionFilter;
        var id_unidad_medidaFilter=this.state.id_unidad_medidaFilter;
        var id_usuarioFilter = this.state.id_usuarioFilter;
        var fecha_tomaFilter = this.state.fecha_tomaFilter;
        var fecha_ingresoFilter=this.state.fecha_ingresoFilter;
        var valorFilter = this.state.valorFilter;

        var filteredData=this.state.v1073161hsFilter.filter(
            function(el){
                return el.id_temp_int_baroFilter.toString().toLowerCase().includes(
                    id_temp_int_baroFilter.toString().trim().toLowerCase()
                )&&
                el.id_estacion.toString().toLowerCase().includes(
                    id_estacionFilter.toString().trim().toLowerCase()
                )
                &&
                el.id_unidad_medida.toString().toLowerCase().includes(
                    id_unidad_medidaFilter.toString().trim().toLowerCase()
                )
                &&
                el.id_usuario.toString().toLowerCase().includes(
                    id_usuarioFilter.toString().trim().toLowerCase()
                )
                &&
                el.fecha_toma.toString().toLowerCase().includes(
                    fecha_tomaFilter.toString().trim().toLowerCase()
                )
                &&
                el.fecha_ingreso.toString().toLowerCase().includes(
                    fecha_ingresoFilter.toString().trim().toLowerCase()
                )
                &&
                el.valor.toString().toLowerCase().includes(
                    valorFilter.toString().trim().toLowerCase()
                )
            }
        );

        this.setState({v1073161hs:filteredData});

    }

    sortResult(prop:any,asc:any){
        var sortedData=this.state.v1073161hsFilter.sort(function(a,b){
            if(asc){
                return (a[prop]>b[prop])?1:((a[prop]<b[prop])?-1:0);
            }
            else{
                return (b[prop]>a[prop])?1:((b[prop]<a[prop])?-1:0);
            }
        });

        this.setState({v1073161hs:sortedData});
    }
 
    changeid_temp_int_baroFilter = (e:any)=>{
        this.state.id_temp_int_baroFilter.valueOf=e.target.value;
        this.FilterFn();
    }
    changeid_estacionFilter = (e:any)=>{
        this.state.id_estacionFilter.valueOf=e.target.value;
        this.FilterFn();
    }
    changeid_unidad_medidaFilter = (e:any)=>{
        this.state.id_unidad_medidaFilter.valueOf=e.target.value;
        this.FilterFn();
    }
    changeid_usuarioFilter = (e:any)=>{
        this.state.id_usuarioFilter.valueOf=e.target.value;
        this.FilterFn();
    }
    changefecha_tomaFilter = (e:any)=>{
        this.state.fecha_tomaFilter.valueOf=e.target.value;
        this.FilterFn();
    }
    changefecha_ingresoFilter = (e:any)=>{
        this.state.fecha_ingresoFilter.valueOf=e.target.value;
        this.FilterFn();
    }

    changevalorFilter = (e:any)=>{
        this.state.valorFilter.valueOf=e.target.value;
        this.FilterFn();
    }



    changeid_estacion =(e:any)=>{
        this.setState({id_estacion:e.target.value});
    }

    changeid_unidad_medida =(e:any)=>{
        this.setState({id_unidad_medida:e.target.value});
    }
    changeid_usuario =(e:any)=>{
        this.setState({id_usuario:e.target.value});
    }
    changefecha_toma =(e:any)=>{
        this.setState({fecha_toma:e.target.value});
    }
    changefecha_ingreso =(e:any)=>{
        this.setState({fecha_ingreso:e.target.value});
    }
    changevalor =(e:any)=>{
        this.setState({valor:e.target.value});
    }
    refreshList(){

        fetch(variables.API_URL+'v1073161h')
        .then(response=>response.json())
        .then(data=>{
            this.setState({v1073161hs:data});
        });
    }
    componentDidMount(){
        this.refreshList();
    }

    editClick(v10:any){
        this.setState({
            
            modalTitle:"Edit Barrometro",
            id_temp_int_baro:v10.id_temp_int_baro,
          
            id_estacion:v10.id_estacion,
            id_unidad_medida:v10.id_unidad_medida,
            id_usuario:v10.id_usuario,
            fecha_toma:v10.fecha_toma,
            fecha_ingreso:v10.fecha_ingreso,
            valor:v10.valor,



        });
    }
    addClick(){
        this.setState({
            modalTitle:"Add Baro",
            id_temp_int_baro:0,
            id_estacion:0,
            id_unidad_medida: 0,
            id_usuario: 0,
            fecha_toma:'',
            fecha_ingreso:'',
            valor: 0,
        });
    }
    createClick(){

        
        fetch(variables.API_URL+'t1073161h',{
            method:'POST',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                id_estacion:this.state.id_estacion,
                id_unidad_medida:this.state.id_unidad_medida,
                id_usuario:this.state.id_usuario,
                fecha_toma:this.state.fecha_toma,
                fecha_ingreso:this.state.fecha_ingreso,
                valor:this.state.valor

            })
        })
        .then(res=>res.json())
        .then((result)=>{
            alert(result);
            this.refreshList();
        },(error)=>{
            alert('Failed');
        })
    }


    updateClick(){
        fetch(variables.API_URL+'v1073161h',{
            method:'PUT',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                id_temp_int_baro:this.state.id_temp_int_baro,
                id_estacion:this.state.id_estacion,
                id_unidad_medida:this.state.id_unidad_medida,
                id_usuario:this.state.id_usuario,
                fecha_toma:this.state.fecha_toma,
                fecha_ingreso:this.state.fecha_ingreso,
                valor:this.state.valor
            })
        })
        .then(res=>res.json())
        .then((result)=>{
            alert(result);
            this.refreshList();
        },(error)=>{
            alert('Failed');
        })
    }

    deleteClick(id:number){
        if(window.confirm('Esta seguro de eliminar el valor?')){
        fetch(variables.API_URL+'v1073161h/'+id,{
            method:'DELETE',
            headers:{
                'Accept':'application/json',
                'Content-Type':'application/json'
            }
        })
        .then(res=>res.json())
        .then((result)=>{
            alert(result);
            this.refreshList();
        },(error)=>{
            alert('Failed');
        })
        }
    }
    

    
    render(){
        const {
            v1073161hs,
            modalTitle,
            id_temp_int_baro,

            id_estacion,
            id_unidad_medida,
            id_usuario,
            fecha_toma,
            fecha_ingreso,
            valor
               }=this.state;
        return(
           
          
            <div>
                 <div className="tablas">
            <button type="button"
            className="btn btn-primary m-2 float-end"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            onClick={()=>this.addClick()}>
                Add Dato
            </button>
                
              <table className="table table-striped">
                  <thead>
                      <tr>
                          <th>
                              
                          id_temp_int_baro
                          </th>
                          <th>
                          id_estacion
                          </th>
                          <th>
                          id_unidad_medida
                          </th>
                          <th>
                          id_usuario
                          </th>
                          <th>
                          fecha_toma
                          </th>
                          <th>
                          fecha_ingreso
                          </th>
                          <th>
                          valor
                          </th>
                      </tr>
                  </thead>
                  <tbody>
                     {v1073161hs.map(v10=>
                        <><tr key={v10.id_temp_int_baro}></tr>
                        <td>{v10.id_temp_int_baro}</td>
                        <td>{v10.id_estacion}</td>
                        <td>{v10.id_unidad_medida}</td>
                        <td>{v10.id_usuario}</td>
                        <td>{v10.fecha_toma}</td>
                        <td>{v10.fecha_ingreso}</td>
                        <td>{v10.valor}</td>
                        <td>


                        <button type="button"
                        className="btn btn-light mr-1"
                     data-bs-toggle="modal"
                     data-bs-target="#exampleModal"
                     onClick={()=>this.editClick(v10)}>

                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-pencil-square" viewBox="0 0 16 16">
                    <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                    <path fillRule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                    </svg>
                       </button>

                <button type="button"
                className="btn btn-light mr-1"
              onClick={()=>this.deleteClick(v10.id_temp_int_baro)}>
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-trash-fill" viewBox="0 0 16 16">
                    <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                    </svg>
                </button>
                        </td>
                        </>
                    )}
                  </tbody>
              </table>

<div className="modal fade"id="exampleModal" aria-hidden="true">
<div className="modal-dialog modal-lg modal-dialog-centered">
<div className="modal-content">
   <div className="modal-header">   
       <h5 className="modal-title">{modalTitle}</h5>
       <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"
       ></button>
   </div>

       <div className="modal-body">
       <div className="input-group mb-3">
        <span className="input-group-text">id_estacion     </span>
        <input type="number" className="form-control"
        value={id_estacion}
        onChange={this.changeid_estacion}/>
       </div>

       <div className="input-group mb-3">
        <span className="input-group-text">id_unidad_medida</span>
        <input type="text" className="form-control"
        value={id_unidad_medida}
        onChange={this.changeid_unidad_medida}/>
       </div>

       <div className="input-group mb-3">
        <span className="input-group-text">id_usuario      </span>
        <input type="text" className="form-control"
        value={id_usuario}
        onChange={this.changeid_usuario}/>
       </div>

       <div className="input-group mb-3">
        <span className="input-group-text">fecha_toma       </span>
        <input type="text" id="start" name="trip-start"  className="form-control required" 
        value={fecha_toma}
        onChange={this.changefecha_toma}/>
       </div>

       <div className="input-group mb-3">
        <span className="input-group-text">fecha_ingreso    </span>
        <input type="text" className="form-control"
        value={fecha_ingreso}
        onChange={this.changefecha_ingreso}/>
       </div>

       <div className="input-group mb-3">
        <span className="input-group-text">valor            </span>
        <input type="text" className="form-control"
        value={valor}
        onChange={this.changevalor}/>
       </div>

        {id_temp_int_baro===0?
        <button type="button"
        className="btn btn-primary float-start"
        onClick={()=>this.createClick()}
        >Create</button>
        :null}

        {id_temp_int_baro!==0?
        <button type="button"
        className="btn btn-primary float-start"
        
        >Update</button>
        :null}

   </div>

</div>
</div> 
</div>

</div>
            </div>
    
        )
    }

}