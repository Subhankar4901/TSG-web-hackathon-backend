(window.webpackJsonp=window.webpackJsonp||[]).push([[19],{976:function(e,t,a){"use strict";a.r(t);var n=a(7),r=a(14),s=a(0),i=a.n(s),o=a(119),c=a(804),l=a(826),m=a(830),u=a(818),d=a(821),b=a(340),f=a(829),p=a(31),h=a(120),w=a(24),v=(a(3),a(9)),y=a(5),E=a(291),g=a(104),j=a.n(g),x=a(164),O=(a(73),a(32)),N="[news] NEW NEWS",I="[news] MAIL NEWS";var S=a(49),C={data:null,categories:[]},F=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:C,t=arguments.length>1?arguments[1]:void 0;switch(t.type){case N:return Object(n.a)({},e,{data:t.payload});case I:return Object(n.a)({},e,t.payload);default:return e}},k=Object(S.d)({news:F}),W=(a(103),a(853),a(851),Object(f.a)(function(e){return{eventImageFeaturedStar:{position:"absolute",top:0,right:0,color:b.a[400],opacity:0},eventImageUpload:{transitionProperty:"box-shadow",transitionDuration:e.transitions.duration.short,transitionTimingFunction:e.transitions.easing.easeInOut},eventImageItem:{transitionProperty:"box-shadow",transitionDuration:e.transitions.duration.short,transitionTimingFunction:e.transitions.easing.easeInOut,"&:hover":{"& $eventImageFeaturedStar":{opacity:.8}},"&.featured":{pointerEvents:"none",boxShadow:e.shadows[3],"& $eventImageFeaturedStar":{opacity:1},"&:hover $eventImageFeaturedStar":{opacity:1}}}}}));t.default=Object(E.a)("news",k)(function(e){var t=Object(y.b)(),a=Object(y.c)(function(e){return e.news.news}),b=(Object(y.c)(function(e){return e.auth.user}),W(e),Object(s.useState)(0)),f=Object(r.a)(b,2),E=f[0],g=f[1],S=Object(h.b)(null),C=S.form,F=S.handleChange,k=S.setForm,T=Object(s.useState)(null),B=Object(r.a)(T,2);return B[0],B[1],Object(s.useEffect)(function(){t({type:N,payload:{description:"",active:!0}})},[t]),Object(s.useEffect)(function(){a.data&&!C&&k(Object(n.a)({},a.data))},[C,a.data,k]),i.a.createElement(p.n,{classes:{toolbar:"p-0",header:"min-h-72 h-72 sm:h-136 sm:min-h-136"},header:i.a.createElement("div",{className:"flex flex-1 w-full items-center justify-between"},i.a.createElement("div",{className:"flex flex-col items-start max-w-full"},i.a.createElement(p.b,{animation:"transition.slideRightIn",delay:300},i.a.createElement(o.a,{className:"normal-case flex items-center sm:mb-12",component:w.a,role:"button",to:"/",color:"inherit"},i.a.createElement(c.a,{className:"mr-4 text-20"},"arrow_back"),"events")),i.a.createElement("div",{className:"flex items-center max-w-full"},i.a.createElement(p.b,{animation:"transition.expandIn",delay:300},i.a.createElement("img",{className:"w-32 sm:w-48 mr-8 sm:mr-16 rounded",src:"assets/images/ecommerce/product-image-placeholder.png"})),i.a.createElement("div",{className:"flex flex-col min-w-0"},i.a.createElement(p.b,{animation:"transition.slideLeftIn",delay:300},i.a.createElement(o.a,{className:"text-16 sm:text-20 truncate"},"Mail News")),i.a.createElement(p.b,{animation:"transition.slideLeftIn",delay:300},i.a.createElement(o.a,{variant:"caption"},"Send any news to all the users"))))),i.a.createElement(p.b,{animation:"transition.slideRightIn",delay:300},i.a.createElement(l.a,{className:"whitespace-no-wrap",variant:"contained",disabled:!!v.a.isEqual(a.data,C),onClick:function(){return t(function(e){var t=fetch("/api/news/mailNews/",{method:"POST",body:e,credentials:"include"});return function(e){return t.then(function(){var t=Object(x.a)(j.a.mark(function t(a){var n;return j.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,a.json();case 2:return n=t.sent,e(Object(O.B)({message:n.message})),t.abrupt("return",e({type:I,payload:n}));case 5:case"end":return t.stop()}},t)}));return function(e){return t.apply(this,arguments)}}())}}(C))}},"Mail"))),contentToolbar:i.a.createElement(m.a,{value:E,onChange:function(e,t){g(t)},indicatorColor:"secondary",textColor:"secondary",variant:"scrollable",scrollButtons:"auto",classes:{root:"w-full h-64"}},i.a.createElement(u.a,{className:"h-64 normal-case",label:"Details"})),content:C&&i.a.createElement("div",{className:"p-16 sm:p-24 max-w-2xl"},0===E&&i.a.createElement("div",{id:"event-form"},i.a.createElement(d.a,{className:"mt-8 mb-16",id:"subject",name:"subject",onChange:F,label:"Subject",type:"text",value:C.subject?C.subject:"",multiline:!0,rows:1,variant:"outlined",fullWidth:!0}),i.a.createElement(d.a,{className:"mt-8 mb-16",id:"body",name:"body",onChange:F,label:"Body",type:"text",value:C.body?C.body:"",multiline:!0,rows:1,variant:"outlined",fullWidth:!0}))),innerScroll:!0})})}}]);