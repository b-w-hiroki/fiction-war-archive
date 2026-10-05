def env(color='0xffd27a',glow='0xffa040',pos=(-90,30,160),extra='',special='const SPECIAL={update(){}};'):
    return f"""const STAR=new THREE.Vector3({pos[0]},{pos[1]},{pos[2]});
const sunM=new THREE.Mesh(new THREE.SphereGeometry(26,48,32),new THREE.MeshBasicMaterial({{color:{color}}}));sunM.position.copy(STAR);scene.add(sunM);
[[160,{glow},.7],[280,{glow},.3]].forEach(([s,c,o])=>{{const g=new THREE.Sprite(new THREE.SpriteMaterial({{map:glowTex,color:c,transparent:true,opacity:o,blending:THREE.AdditiveBlending,depthWrite:false}}));g.scale.set(s,s,1);g.position.copy(STAR);scene.add(g)}});
const pl=new THREE.PointLight(0xfff0d8,1.2,0);pl.position.copy(STAR);scene.add(pl);
scene.add(new THREE.AmbientLight(0x4a5a78,.6));
const fill=new THREE.DirectionalLight(0x9fb6ff,.35);fill.position.set(60,80,-80);scene.add(fill);
{extra}
{special}
"""

def fort(name='イゼルローン要塞',sub='',side='E',pos=(0,0,-55),color='0xcfd6df',r=11,extra_labels=()):
    """要塞の球体とラベル。extra_labels: [(text,sub,side,(x,y,z))]"""
    ex=f"""const FORT=new THREE.Mesh(new THREE.SphereGeometry({r},48,32),new THREE.MeshLambertMaterial({{color:{color},emissive:0x1a2430}}));FORT.position.set({pos[0]},{pos[1]},{pos[2]});scene.add(FORT);\n"""
    labs=''.join([f"{{const l=sprite('{t}','{s}',CSS.{sd},2.4);l.position.set({p[0]},{p[1]},{p[2]});scene.add(l)}}" for t,s,sd,p in extra_labels])
    sp=f"""const SPECIAL={{lab:null,reset(){{if(!this.lab){{this.lab=sprite('{name}','{sub}',CSS.{side},3);this.lab.position.set({pos[0]},{pos[1]+r+2},{pos[2]});scene.add(this.lab);{labs}}}}},update(){{}}}};"""
    return ex,sp

CANNON=r"""
function cannonFX(a,b,col,w){const d=new THREE.Vector3().subVectors(b,a),L=d.length();const m=new THREE.Mesh(new THREE.CylinderGeometry(w,w,L,12,1,true),new THREE.MeshBasicMaterial({color:col,transparent:true,opacity:1,blending:THREE.AdditiveBlending,depthWrite:false}));
 m.position.copy(a).addScaledVector(d,.5);m.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),d.normalize());scene.add(m);return {m,life:1.2}}
const BEAMS=[];function beamsUpdate(dt){for(let i=BEAMS.length-1;i>=0;i--){const b=BEAMS[i];b.life-=dt;b.m.material.opacity=Math.max(0,b.life);if(b.life<=0){scene.remove(b.m);b.m.geometry.dispose();BEAMS.splice(i,1)}}}
"""
def fort_cannon(name,sub,side,pos,target_unit,phase,delay=1.5,color='0xcfd6df',r=11,beam='0xbfe8ff'):
    """要塞＋指定場面で主砲を指定部隊へ撃つ"""
    ex,_=fort(name,sub,side,pos,color,r)
    sp=f"""const SPECIAL={{lab:null,fired:false,reset(){{this.fired=false;if(!this.lab){{this.lab=sprite('{name}','{sub}',CSS.{side},3);this.lab.position.set({pos[0]},{pos[1]+r+2},{pos[2]});scene.add(this.lab)}}}},
 update(now,dt){{const t=now-phaseStart;if(phase==={phase}&&!this.fired&&t>{delay}){{this.fired=true;const u=units.find(o=>o.name==='{target_unit}');const b=new THREE.Vector3(u.x,u.y,u.z);BEAMS.push(cannonFX(FORT.position,b,{beam},1.6));for(let k=0;k<10;k++)boom([u.x+(Math.random()-.5)*14,u.y+(Math.random()-.5)*6,u.z+(Math.random()-.5)*14],true,0xffc080)}}beamsUpdate(dt)}}}};"""
    return ex+CANNON,sp
