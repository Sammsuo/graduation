webpackJsonp([1],{"57JN":function(e,t){},Egw9:function(e,t){},G3ho:function(e,t){},HmD5:function(e,t){},IbvA:function(e,t){},NHnr:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},staticRenderFns:[]};var n=a("VU/8")({name:"App"},s,!1,function(e){a("iPNe")},"data-v-6a8e64da",null).exports,r=a("7+uW"),i=a("/ocq"),l=a("zL8q"),o=a.n(l),c=(a("tvR6"),{render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"login-head"},[a("el-form",{ref:"form",staticClass:"login-box",attrs:{model:e.form,rules:e.rules,"label-width":"80px"}},[a("h3",{staticClass:"login-title"},[e._v("登录")]),e._v(" "),a("el-form-item",{attrs:{label:"账号",prop:"username"}},[a("el-input",{attrs:{type:"text",placeholder:"请输入账号"},model:{value:e.form.username,callback:function(t){e.$set(e.form,"username",t)},expression:"form.username"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"密码",prop:"password"}},[a("el-input",{attrs:{type:"password",placeholder:"请输入密码"},nativeOn:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.submitform(e.form)}},model:{value:e.form.password,callback:function(t){e.$set(e.form,"password",t)},expression:"form.password"}})],1),e._v(" "),a("el-form-item",[a("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.submitform(e.form)}}},[e._v("登录")])],1)],1)],1)},staticRenderFns:[]});var u=a("VU/8")({name:"Login",data:function(){return{form:{username:"",password:""},rules:{username:[{required:!0,message:"请输入账号",trigger:"blur"}],password:[{required:!0,message:"请输入密码",trigger:"blur"}]},msg:""}},methods:{submitform:function(e){this.$router.push("/main")}}},c,!1,function(e){a("z17t")},"data-v-9aeb8704",null).exports,d={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"el-head"},[a("el-header",{staticStyle:{"text-align":"right","font-size":"12px"}},[a("span",{staticClass:"header-title"},[e._v("简单测试平台")]),e._v(" "),a("el-dropdown",[a("i",{staticClass:"el-icon-setting",staticStyle:{"margin-right":"15px"}}),e._v(" "),a("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[a("el-dropdown-item",[e._v("修改密码")]),e._v(" "),a("el-dropdown-item",[e._v("退出登录")])],1)],1),e._v(" "),a("span",[e._v("SAM")])],1),e._v(" "),a("div",{staticClass:"el-asider"},[a("el-container",{staticStyle:{border:"1px solid #eee"}},[a("el-aside",{attrs:{width:"200px"}},[a("el-menu",[a("el-submenu",{attrs:{index:"1"}},[a("template",{slot:"title"},[a("i",{staticClass:"el-icon-message"}),e._v("用例编写")]),e._v(" "),a("el-menu-item-group",[a("el-menu-item",{attrs:{index:"1-1"},on:{click:function(t){return e.gotoPage(e.url.url1)}}},[e._v("功能用例")]),e._v(" "),a("el-menu-item",{attrs:{index:"1-2"},on:{click:function(t){return e.gotoPage(e.url.url2)}}},[e._v("接口用例")])],1)],2),e._v(" "),a("el-submenu",{attrs:{index:"2"}},[a("template",{slot:"title"},[a("i",{staticClass:"el-icon-menu"}),e._v("测试方式")]),e._v(" "),a("el-menu-item-group",[a("el-menu-item",{attrs:{index:"2-1"},on:{click:function(t){return e.gotoPage(e.url.url3)}}},[e._v("接口测试")]),e._v(" "),a("el-menu-item",{attrs:{index:"2-2"}},[e._v("压力测试")])],1)],2),e._v(" "),a("el-submenu",{attrs:{index:"3"}},[a("template",{slot:"title"},[a("i",{staticClass:"el-icon-setting"}),e._v("文档校验")]),e._v(" "),a("el-menu-item-group",[a("el-menu-item",{attrs:{index:"3-1"},on:{click:function(t){return e.gotoPage(e.url.url4)}}},[e._v("数据库DDL文件格式校验")])],1)],2)],1)],1)],1)],1)],1)},staticRenderFns:[]};var m={name:"Main",components:{Aside:a("VU/8")({name:"Aside",data:function(){return{url:{url1:"/FunctionCase",url2:"/APICase",url3:"/APITest",url4:"/DDLCheck"}}},methods:{gotoPage:function(e){this.$router.push(e)}}},d,!1,function(e){a("IbvA")},"data-v-7d31a91c",null).exports}},p={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticStyle:{height:"100%",weight:"100%"}},[t("Aside"),this._v(" "),t("div",{staticClass:"right-box"},[t("router-view")],1)],1)},staticRenderFns:[]};var v=a("VU/8")(m,p,!1,function(e){a("Egw9")},"data-v-87270494",null).exports,f={name:"FunctionCase",data:function(){return{list:[{CaseName:"",CasePath:"",CaseStep:"",CaseContition:"",CaseExpect:"",CaseRemark:"",name:"用例1"}],listLong:2}},methods:{remove:function(e){var t=this.list.indexOf(e);for(var a in-1!==t&&(this.list.splice(t,1),this.listLong--),this.list)this.list[a].name="用例"+ ++a},add:function(){var e="用例"+this.listLong++;this.list.push({CaseName:"",CasePath:"",CaseStep:"",CaseContition:"",CaseExpect:"",name:e}),console.log(this.list)},download_be_excel:function(){},upload_to_zentao:function(){}}},h={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticStyle:{height:"100%",padding:"30px"}},[a("span",[e._v("功能用例")]),e._v(" "),a("div",[a("el-form",[a("el-form-item",[a("el-button",{attrs:{type:"primary"},on:{click:e.add}},[e._v("新增")]),e._v(" "),a("el-button",{attrs:{type:"success"}},[e._v("下载")]),e._v(" "),a("el-button",{attrs:{type:"success"}},[e._v("上传")])],1)],1),e._v(" "),a("div",{staticStyle:{"overflow-y":"auto",height:"500px",width:"920px"}},e._l(e.list,function(t){return a("div",[a("el-form",{attrs:{model:t}},[a("el-form-item",{staticStyle:{width:"900px"},attrs:{label:t.name}},[a("el-input",{staticStyle:{width:"150px"},attrs:{placeholder:"用例名"},model:{value:t.CaseName,callback:function(a){e.$set(t,"CaseName",a)},expression:"FuncForm.CaseName"}}),e._v(" "),a("el-input",{staticStyle:{width:"150px"},attrs:{placeholder:"预期结果"},model:{value:t.CaseExpect,callback:function(a){e.$set(t,"CaseExpect",a)},expression:"FuncForm.CaseExpect"}}),e._v(" "),a("el-input",{staticStyle:{width:"150px"},attrs:{placeholder:"备注"},model:{value:t.CaseRemark,callback:function(a){e.$set(t,"CaseRemark",a)},expression:"FuncForm.CaseRemark"}}),e._v(" "),a("br"),e._v(" "),a("el-input",{staticStyle:{width:"233px","margin-left":"48px"},attrs:{type:"textarea",placeholder:"前置条件"},model:{value:t.CaseContition,callback:function(a){e.$set(t,"CaseContition",a)},expression:"FuncForm.CaseContition"}}),e._v(" "),a("el-input",{staticStyle:{width:"233px"},attrs:{type:"textarea",placeholder:"具体步骤"},model:{value:t.CaseStep,callback:function(a){e.$set(t,"CaseStep",a)},expression:"FuncForm.CaseStep"}}),e._v(" "),"用例1"!==t.name?a("el-button",{attrs:{type:"danger"},on:{click:function(t){return e.remove(e.form)}}},[e._v("删除")]):e._e()],1)],1)],1)}),0)],1)])},staticRenderFns:[]};var _=a("VU/8")(f,h,!1,function(e){a("HmD5")},"data-v-17f898d2",null).exports,C={render:function(){var e=this.$createElement;return(this._self._c||e)("div",[this._v("haha")])},staticRenderFns:[]};var x=a("VU/8")({name:"FirstPage"},C,!1,function(e){a("XCM8")},"data-v-5af572e0",null).exports,g={name:"APICase",data:function(){return{list:[{CaseName:"",CaseUrl:"",CaseMethod:"",CaseHeader:"",CaseParams:"",name:"用例1"}],listLong:2}},methods:{remove:function(e){var t=this.list.indexOf(e);for(var a in-1!==t&&(this.list.splice(t,1),this.listLong--),this.list)this.list[a].name="用例"+ ++a},add:function(){var e="用例"+this.listLong++;this.list.push({CaseName:"",CaseUrl:"",CaseMethod:"",CaseHeader:"",CaseParams:"",name:e}),console.log(this.list)},download_be_excel:function(){},upload_to_zentao:function(){}}},y={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticStyle:{height:"100%",padding:"30px"}},[a("span",[e._v("接口用例")]),e._v(" "),a("div",[a("el-form",[a("el-form-item",[a("el-button",{attrs:{type:"primary"},on:{click:e.add}},[e._v("新增")]),e._v(" "),a("el-button",{attrs:{type:"success"}},[e._v("下载")]),e._v(" "),a("el-button",{attrs:{type:"success"}},[e._v("上传")])],1)],1),e._v(" "),a("div",{staticStyle:{"overflow-y":"auto",height:"500px",width:"920px"}},e._l(e.list,function(t){return a("div",[a("el-form",{attrs:{model:t}},[a("el-form-item",{staticStyle:{width:"900px"},attrs:{label:t.name}},[a("el-input",{staticStyle:{width:"150px"},attrs:{placeholder:"用例名"},model:{value:t.CaseName,callback:function(a){e.$set(t,"CaseName",a)},expression:"APIForm.CaseName"}}),e._v(" "),a("el-input",{staticStyle:{width:"200px"},attrs:{placeholder:"Url"},model:{value:t.CaseUrl,callback:function(a){e.$set(t,"CaseUrl",a)},expression:"APIForm.CaseUrl"}}),e._v(" "),a("el-input",{staticStyle:{width:"100px"},attrs:{placeholder:"调用方式"},model:{value:t.CaseMethod,callback:function(a){e.$set(t,"CaseMethod",a)},expression:"APIForm.CaseMethod"}}),e._v(" "),a("br"),e._v(" "),a("el-input",{staticStyle:{width:"233px","margin-left":"48px"},attrs:{type:"textarea",placeholder:"headers"},model:{value:t.CaseHeader,callback:function(a){e.$set(t,"CaseHeader",a)},expression:"APIForm.CaseHeader"}}),e._v(" "),a("el-input",{staticStyle:{width:"233px"},attrs:{type:"textarea",placeholder:"内容"},model:{value:t.CaseParams,callback:function(a){e.$set(t,"CaseParams",a)},expression:"APIForm.CaseParams"}}),e._v(" "),"用例1"!==t.name?a("el-button",{attrs:{type:"danger"},on:{click:function(a){return e.remove(t)}}},[e._v("删除")]):e._e()],1)],1)],1)}),0)],1)])},staticRenderFns:[]};var b=a("VU/8")(g,y,!1,function(e){a("G3ho")},"data-v-7a79b908",null).exports,P=a("mvHQ"),w=a.n(P),F={name:"APITest",data:function(){return{APIForm:{CaseUrl:"",CaseMethod:"",CaseHeader:"",CaseParams:"",name:"调试"},all:"sadfasdf"}},methods:{postUrl:function(e){var t=this;this.$axios({method:"post",url:"getRequest/post/",data:{params:e.CaseParams,requestUrl:e.CaseUrl,Headers:e.CaseHeader},dataType:"json"}).then(function(e){console.log(e.data.data),t.all=w()(e.data.data),console.log(e)})},getUrl:function(){},getReapone:function(){}}},k={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("span",[e._v("接口测试")]),e._v(" "),a("div",[a("el-form",[a("el-form-item",[a("el-button",{attrs:{type:"primary"}},[e._v("上传")]),e._v(" "),a("el-button",{attrs:{type:"success"}},[e._v("跑接口")])],1)],1)],1),e._v(" "),a("div",{staticClass:"requestArea",staticStyle:{"overflow-y":"auto",height:"150px",width:"920px"}},[a("div",[a("el-form",{attrs:{model:e.APIForm}},[a("el-form-item",{staticStyle:{width:"900px"},attrs:{label:e.APIForm.name}},[a("el-input",{staticStyle:{width:"200px","margin-left":"8px"},attrs:{placeholder:"Url"},model:{value:e.APIForm.CaseUrl,callback:function(t){e.$set(e.APIForm,"CaseUrl",t)},expression:"APIForm.CaseUrl"}}),e._v(" "),a("el-input",{staticStyle:{width:"100px"},attrs:{placeholder:"调用方式"},model:{value:e.APIForm.CaseMethod,callback:function(t){e.$set(e.APIForm,"CaseMethod",t)},expression:"APIForm.CaseMethod"}}),e._v(" "),a("br"),e._v(" "),a("el-input",{staticStyle:{width:"233px","margin-left":"48px"},attrs:{type:"textarea",placeholder:"headers"},model:{value:e.APIForm.CaseHeader,callback:function(t){e.$set(e.APIForm,"CaseHeader",t)},expression:"APIForm.CaseHeader"}}),e._v(" "),a("el-input",{staticStyle:{width:"233px"},attrs:{type:"textarea",placeholder:"内容"},model:{value:e.APIForm.CaseParams,callback:function(t){e.$set(e.APIForm,"CaseParams",t)},expression:"APIForm.CaseParams"}}),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.postUrl(e.APIForm)}}},[e._v("发送")])],1)],1)],1)]),e._v(" "),a("div",{staticClass:"responeArea"},[a("span",[e._v("响应报文")]),e._v(" "),a("div",{staticStyle:{height:"400px"}},[a("el-input",{staticClass:"requestRead",staticStyle:{"margin-left":"48px",width:"480px"},attrs:{type:"textarea",rows:10},model:{value:e.all,callback:function(t){e.all=t},expression:"all"}})],1)])])},staticRenderFns:[]};var A=a("VU/8")(F,k,!1,function(e){a("tsJo")},"data-v-3680724e",null).exports,S={render:function(){var e=this.$createElement;return(this._self._c||e)("div",[this._v("DDL文档校验")])},staticRenderFns:[]};var I=a("VU/8")({name:"DDLCheck"},S,!1,function(e){a("57JN")},"data-v-30969a26",null).exports;r.default.use(i.a);var $=new i.a({routes:[{path:"",name:"Login",component:u},{path:"/main",name:"Main",component:v,children:[{path:"/FirstPage",name:"FirstPage",component:x},{path:"/FunctionCase",name:"FunctionCase",component:_},{path:"/APICase",name:"APICase",component:b},{path:"/APITest",name:"APITest",component:A},{path:"/DDLCheck",name:"DDLCheck",component:I}]}]}),U=a("mtWM"),R=a.n(U);r.default.use(i.a),r.default.use(o.a),R.a.defaults.headers.post["Content-Type"]="application/json",r.default.prototype.$axios=R.a,new r.default({el:"#app",router:$,render:function(e){return e(n)}})},XCM8:function(e,t){},iPNe:function(e,t){},tsJo:function(e,t){},tvR6:function(e,t){},z17t:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.e29c618e6b51144ef3cb.js.map