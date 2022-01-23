(window.webpackJsonp=window.webpackJsonp||[]).push([[19],{979:function(e,t,a){"use strict";a.r(t);var n=a(14),l=a(0),c=a.n(l),r=a(119),o=a(804),i=a(821),s=a(755),m=a(767),u=a(770),f=a(771),d=a(807),p=a(816),v=a(828),h=a(813),E=a(842),x=a(826),y=a(824),b=a(829),w=a(397),g=a(31),N=a(5),j=a(291),O=a(3),C=a(9),S=a(24),_=a(73),k=a.n(_),T=(a(63),"[ACHIEVEMENTS] GET_ACHIEVEMENT"),I="[ACHIEVEMENTS] GET_CATEGORIES";var A=a(49),L=a(7),D={data:null,categories:[]},G=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:D,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case T:return Object(L.a)({},e,{data:t.payload});case I:return Object(L.a)({},e,{categories:t.payload});default:return e}},M=Object(A.d)({achievement:G}),P=(a(103),a(941),Object(b.a)(function(e){return{header:{background:"linear-gradient(to right, "+e.palette.primary.dark+" 0%, "+e.palette.primary.main+" 100%)",color:e.palette.getContrastText(e.palette.primary.main)},headerIcon:{position:"absolute",top:-64,left:0,opacity:.04,fontSize:512,width:512,height:512,pointerEvents:"none"}}}));t.default=Object(j.a)("achievements",M)(function(e){var t=Object(N.b)(),a=Object(N.c)(function(e){return e.achievements.achievement.data}),b=Object(N.c)(function(e){return e.achievements.achievement.categories}),j=(Object(N.c)(function(e){return e.auth.user}),P(e)),_=Object(w.a)(),A=Object(l.useState)(null),L=Object(n.a)(A,2),D=L[0],G=L[1],M=Object(l.useState)(""),V=Object(n.a)(M,2),H=V[0],W=V[1],J=Object(l.useState)("all"),U=Object(n.a)(J,2),z=U[0],B=U[1];return Object(l.useEffect)(function(){t(function(){var e=k.a.get("/api/achievement/student/getAchievements",{withCredentials:!0});return function(t){return e.then(function(e){console.log(e),t({type:T,payload:e.data.achievements})})}}()),t(function(){var e=[{id:0,value:"Technology",label:"Technology",color:"#6a26cd"},{id:1,value:"Social and Culture",label:"Social and Culture",color:"#ffd557"},{id:2,value:"Sports and Games",label:"Sports and Games",color:"#5fff56"},{id:3,value:"Students' Welfare",label:"Students' Welfare",color:"#ff56a2"}];return function(t){return t({type:I,payload:e})}}())},[t]),Object(l.useEffect)(function(){a&&G(0===H.length&&"all"===z?(console.log(a),a):C.a.filter(a,function(e){return"all"!==z&&e.event_type.toLowerCase()!==z.toLowerCase()?(console.log(e.event_type,z),!1):e.event_title.toLowerCase().includes(H.toLowerCase())}))},[a,H,z]),c.a.createElement("div",{className:"flex flex-col flex-1 w-full"},c.a.createElement("div",{className:Object(O.a)(j.header,"relative overflow-hidden flex flex-col flex-shrink-0 items-center justify-center text-center p-16 sm:p-24 h-200 sm:h-288")},c.a.createElement(g.b,{animation:"transition.slideUpIn",duration:400,delay:100},c.a.createElement(r.a,{color:"inherit",className:"text-24 sm:text-40 font-light"},"Achievements")),c.a.createElement(g.b,{duration:400,delay:600},c.a.createElement(r.a,{variant:"subtitle1",color:"inherit",className:"mt-8 sm:mt-16 mx-auto max-w-512"},c.a.createElement("span",{className:"opacity-75"},"Your achievements in various events that you participated."))),c.a.createElement(o.a,{className:j.headerIcon},"airplanemode_active")),c.a.createElement("div",{className:"flex flex-col flex-1 max-w-2xl w-full mx-auto px-8 sm:px-16 py-24"},c.a.createElement("div",{className:"flex flex-col flex-shrink-0 sm:flex-row items-center justify-between py-24"},c.a.createElement(i.a,{label:"Search for a event",placeholder:"Enter a keyword...",className:"flex w-full sm:w-320 mb-16 sm:mb-0 mx-16",value:H,inputProps:{"aria-label":"Search"},onChange:function(e){W(e.target.value)},variant:"outlined",InputLabelProps:{shrink:!0}}),c.a.createElement(s.a,{className:"flex w-full sm:w-320 mx-16",variant:"outlined"},c.a.createElement(m.a,{htmlFor:"category-label-placeholder"},"Category"),c.a.createElement(u.a,{value:z,onChange:function(e){B(e.target.value)},input:c.a.createElement(f.a,{labelWidth:9*"category".length,name:"category",id:"category-label-placeholder"})},c.a.createElement(d.a,{value:"all"},c.a.createElement("em",null,"All")),b.map(function(e){return c.a.createElement(d.a,{value:e.value,key:e.id},e.label)})))),Object(l.useMemo)(function(){return D&&(D.length>0?c.a.createElement(g.c,{enter:{animation:"transition.slideUpBigIn"},className:"flex flex-wrap py-24"},D.map(function(e){var t=b.find(function(t){return t.value.toLowerCase()===e.event_type.toLowerCase()});return c.a.createElement("div",{className:"w-full pb-24 sm:w-1/2 lg:w-1/3 sm:p-16",key:e.id},c.a.createElement(p.a,{elevation:1,className:"flex flex-col h-256"},c.a.createElement("div",{className:"flex flex-shrink-0 items-center justify-between px-24 h-64",style:{background:t.color,color:_.palette.getContrastText(t.color)}},c.a.createElement(r.a,{className:"font-medium truncate",color:"inherit"},t.label),c.a.createElement("div",{className:"flex items-center justify-center opacity-75"},c.a.createElement(o.a,{className:"text-20 mr-8",color:"inherit"},"date_range"),c.a.createElement("div",{className:"text-16 whitespace-no-wrap"},Math.floor((new Date(e.end)-new Date(e.start))/864e5)," days"))),c.a.createElement(v.a,{className:"flex flex-col flex-auto items-center justify-center"},c.a.createElement(r.a,{className:"text-center text-16 font-400"},"Position ",c.a.createElement(o.a,null,"directions_run")," ",c.a.createElement("strong",null,e.position)," in",c.a.createElement(S.a,{to:{pathname:"/events/".concat(e.event_id,"/").concat(e.event_title),state:{prevPath:window.location.pathname}},className:"justify-start px-3",color:"secondary"},e.event_title)),c.a.createElement(r.a,{className:"text-center text-13 font-600 mt-4",color:"textSecondary"},new Date(e.start).toDateString()," - ",new Date(e.end).toDateString())),c.a.createElement(h.a,null),c.a.createElement(E.a,{className:"justify-center"},e.certificate_uploaded?c.a.createElement(x.a,{className:"justify-start px-32",color:"secondary"},c.a.createElement("a",{href:e.certificate,target:"_blank"},"Certificate")):c.a.createElement(x.a,{to:{pathname:"/events/".concat(e.event_id,"/").concat(e.event_title),state:{prevPath:window.location.pathname}},component:S.a,className:"justify-start px-32",color:"secondary"},"View Event")),c.a.createElement(y.a,{className:"w-full",variant:"determinate",value:0,color:"secondary"})))})):c.a.createElement("div",{className:"flex flex-1 items-center justify-center"},c.a.createElement(r.a,{color:"textSecondary",className:"text-24 my-24"},"No achievements found!")))},[b,D,_.palette])))})}}]);