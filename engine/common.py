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
const BEAMS=[],WAVES=[];
function shockwaveFX(p,col=0xffd080,max=22){const m=new THREE.Mesh(new THREE.RingGeometry(1,1.25,64),new THREE.MeshBasicMaterial({color:col,transparent:true,opacity:.9,blending:THREE.AdditiveBlending,depthWrite:false,side:THREE.DoubleSide}));m.position.copy(p);m.rotation.x=-Math.PI/2;scene.add(m);return {m,life:1,maxLife:1,max}}
function beamsUpdate(dt){
 for(let i=BEAMS.length-1;i>=0;i--){const b=BEAMS[i];b.life-=dt;b.m.material.opacity=Math.max(0,b.life);if(b.life<=0){scene.remove(b.m);b.m.geometry.dispose();BEAMS.splice(i,1)}}
 for(let i=WAVES.length-1;i>=0;i--){const w=WAVES[i];w.life-=dt;const p=1-Math.max(0,w.life/w.maxLife),sc=1+(w.max-1)*p;w.m.scale.set(sc,sc,1);w.m.material.opacity=.9*(1-p);if(w.life<=0){scene.remove(w.m);w.m.geometry.dispose();WAVES.splice(i,1)}}
}
"""
def fort_cannon(name,sub,side,pos,target_unit,phase,delay=1.5,color='0xcfd6df',r=11,beam='0xbfe8ff'):
    """要塞＋指定場面で主砲を指定部隊へ撃つ"""
    ex,_=fort(name,sub,side,pos,color,r)
    sp=f"""const SPECIAL={{lab:null,fired:false,reset(){{this.fired=false;if(!this.lab){{this.lab=sprite('{name}','{sub}',CSS.{side},3);this.lab.position.set({pos[0]},{pos[1]+r+2},{pos[2]});scene.add(this.lab)}}}},
 update(now,dt){{const t=now-phaseStart;if(phase==={phase}&&!this.fired&&t>{delay}){{this.fired=true;const u=units.find(o=>o.name==='{target_unit}');const b=new THREE.Vector3(u.x,u.y,u.z);BEAMS.push(cannonFX(FORT.position,b,{beam},1.6));for(let k=0;k<10;k++)boom([u.x+(Math.random()-.5)*14,u.y+(Math.random()-.5)*6,u.z+(Math.random()-.5)*14],true,0xffc080)}}beamsUpdate(dt)}}}};"""
    return ex+CANNON,sp


# ---------- 地球圏・地上戦の環境 ----------

def ground(low='0x3d5a3a', high='0x8a8268', size=260, amp=6, y=-4, seed=1, water=None):
    """地上戦の地形。units は y=0 付近に浮かせて置く。water='0x2a5a78' で低地を水面に"""
    w = f"""const wat=new THREE.Mesh(new THREE.PlaneGeometry({size},{size}),new THREE.MeshLambertMaterial({{color:{water},transparent:true,opacity:.85}}));wat.rotation.x=-Math.PI/2;wat.position.y=({y})-.2;scene.add(wat);""" if water else ''
    return f"""
(function(){{const S={size},N=110,g=new THREE.PlaneGeometry(S,S,N,N);g.rotateX(-Math.PI/2);const p=g.attributes.position,c=new Float32Array(p.count*3),lo=new THREE.Color({low}),hi=new THREE.Color({high}),t=new THREE.Color();
 for(let i=0;i<p.count;i++){{const x=p.getX(i),z=p.getZ(i);let h=0,f=.012,a=1;for(let o=0;o<4;o++){{h+=a*(Math.sin(x*f+{seed}*1.7+o)*Math.cos(z*f*1.3+{seed}+o*2.1));f*=2.1;a*=.48}}
  h=h*{amp}+({y});p.setY(i,h);t.copy(lo).lerp(hi,Math.min(1,Math.max(0,(h-({y})+{amp})/({amp}*2))));c.set([t.r,t.g,t.b],i*3)}}
 g.setAttribute('color',new THREE.BufferAttribute(c,3));g.computeVertexNormals();
 const m=new THREE.Mesh(g,new THREE.MeshLambertMaterial({{vertexColors:true}}));scene.add(m);{w}
 scene.background=new THREE.Color(0x6f8297);scene.fog=new THREE.Fog(0x6f8297,320,1100);}})();
"""


def sky_env(sun=(80, 120, 40)):
    """地上用の光源（恒星は置かない）"""
    return f"""const SUNL=new THREE.DirectionalLight(0xfff2dc,1.0);SUNL.position.set({sun[0]},{sun[1]},{sun[2]});scene.add(SUNL);
scene.add(new THREE.HemisphereLight(0xcfe0f0,0x4a4a3a,.75));
"""


def planet(pos=(0, -260, 0), r=200, color='0x2f6fb0', land='0x5a8a4a', label=None, side='A'):
    """地球などの惑星（大気の輪郭つき）"""
    lab = f"setTimeout(()=>{{const l=sprite('{label[0]}','{label[1]}',CSS.{side},3);l.position.set({pos[0]},{pos[1]+r+6},{pos[2]});scene.add(l)}},0);" if label else ''
    return f"""
(function(){{const c=document.createElement('canvas');c.width=512;c.height=256;const x=c.getContext('2d');x.fillStyle='#{color[2:]}';x.fillRect(0,0,512,256);
 for(let i=0;i<70;i++){{x.fillStyle=i%9?'#{land[2:]}':'#e8eef2';x.beginPath();x.ellipse(hs(i,61)*512,30+hs(62,i)*196,10+hs(i,63)*46,6+hs(i,64)*24,hs(i,65)*3,0,6.3);x.fill()}}
 const tex=new THREE.CanvasTexture(c);const m=new THREE.Mesh(new THREE.SphereGeometry({r},64,40),new THREE.MeshLambertMaterial({{map:tex}}));m.position.set({pos[0]},{pos[1]},{pos[2]});scene.add(m);
 const a=new THREE.Mesh(new THREE.SphereGeometry({r}*1.025,64,40),new THREE.MeshBasicMaterial({{color:0x8fc4ff,transparent:true,opacity:.18,side:THREE.BackSide}}));a.position.copy(m.position);scene.add(a);
 window.PLANET=m;{lab}}})();
"""


def colony(pos=(0, 0, 0), rot=(0, 0, 0), length=40, r=4, name='COLONY'):
    """円筒形のスペースコロニー"""
    return f"""
const {name}=new THREE.Group();(function(){{const b=new THREE.Mesh(new THREE.CylinderGeometry({r},{r},{length},24,1),new THREE.MeshLambertMaterial({{color:0xb8c0c8,emissive:0x1a2028}}));{name}.add(b);
 for(let i=0;i<3;i++){{const m=new THREE.Mesh(new THREE.BoxGeometry(.4,{length}*.9,{r}*2.4),new THREE.MeshLambertMaterial({{color:0x8fa6c0,emissive:0x101820}}));m.rotation.y=i*2.09;m.position.set(Math.cos(i*2.09)*{r}*1.6,0,Math.sin(i*2.09)*{r}*1.6);{name}.add(m)}}
 {name}.position.set({pos[0]},{pos[1]},{pos[2]});{name}.rotation.set({rot[0]},{rot[1]},{rot[2]});scene.add({name})}})();
"""


def rock_fortress(pos=(0, 0, -60), r=12, shape='solomon', name='FORT'):
    """宇宙要塞。solomon=十字に突起の岩塊、abaoaqu=傘形"""
    if shape == 'abaoaqu':
        body = f"""const a=new THREE.Mesh(new THREE.ConeGeometry({r}*1.5,{r}*.7,10,1,false),M);a.position.y={r}*.45;{name}.add(a);const a2=new THREE.Mesh(new THREE.CylinderGeometry({r}*1.5,{r}*1.3,{r}*.25,10),M);a2.position.y={r}*.0;{name}.add(a2);
 const s=new THREE.Mesh(new THREE.CylinderGeometry({r}*.4,{r}*.2,{r}*1.8,8),M);s.position.y=-{r}*1.0;{name}.add(s);"""
    else:
        body = f"""for(let i=0;i<6;i++){{const d=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]][i];const b=new THREE.Mesh(new THREE.DodecahedronGeometry({r}*(i<4?.55:.4),0),M);b.position.set(d[0]*{r}*.75,d[1]*{r}*.6,d[2]*{r}*.6);{name}.add(b)}}
 {name}.add(new THREE.Mesh(new THREE.DodecahedronGeometry({r}*.7,1),M));"""
    return f"""
const {name}=new THREE.Group();(function(){{const M=new THREE.MeshLambertMaterial({{color:0x8a8478,emissive:0x1a1610,flatShading:true}});{body}
 {name}.position.set({pos[0]},{pos[1]},{pos[2]});scene.add({name})}})();
"""


# ---------- 組み合わせて使う演出 ----------
# 各関数は (extra_js, special_part_js) を返す。specials() で SPECIAL にまとめる。

def labels(items):
    """固定ラベル。items: [(text,sub,side,(x,y,z),scale)]"""
    js = ''.join(f"{{const l=sprite('{t}','{s}',CSS.{sd},{sc}*1.6);l.position.set({p[0]},{p[1]},{p[2]});scene.add(l)}}" for t, s, sd, p, sc in items)
    return '', f"{{done:false,reset(){{if(!this.done){{this.done=true;{js}}}}}}}"


def move_obj(name, keys, secs=4):
    """物体を場面ごとに動かす。keys: {場面: (x,y,z)}。場面の開始から secs 秒かけて移動"""
    kj = ','.join(f"{k}:[{v[0]},{v[1]},{v[2]}]" for k, v in keys.items())
    return '', (f"{{K:{{{kj}}},a:null,b:null,t0:0,reset(i){{let k=-1;for(const j in this.K)if(+j<=i)k=Math.max(k,+j);if(k<0)return;"
                f"this.a={name}.position.clone();this.b=new THREE.Vector3(...this.K[k]);this.t0=VT}},"
                f"update(now){{if(!this.b)return;const p=Math.min(1,(now-this.t0)/{secs});{name}.position.lerpVectors(this.a,this.b,ease(p))}}}}")


def shot(src, target_unit, phase, delay=1.5, beam='0xbfe8ff', w=1.6, booms=10, wave=False):
    """指定場面で src（座標）から部隊へ太いビームを撃つ。wave=True で大規模着弾の衝撃波を追加"""
    wave_js = "WAVES.push(shockwaveFX(b,0xffd080,28));" if wave else ""
    return CANNON, (f"{{fired:false,reset(){{this.fired=false}},update(now){{const t=now-phaseStart;if(phase==={phase}&&!this.fired&&t>{delay}){{this.fired=true;"
                    f"const u=units.find(o=>o.name==='{target_unit}');const b=new THREE.Vector3(u.x,u.y,u.z);BEAMS.push(cannonFX(new THREE.Vector3({src[0]},{src[1]},{src[2]}),b,{beam},{w}));{wave_js}"
                    f"for(let k=0;k<{booms};k++)boom([u.x+(Math.random()-.5)*14,u.y+(Math.random()-.5)*6,u.z+(Math.random()-.5)*14],true,0xffc080)}}}}}}")


def specials(*parts):
    """(extra, part) の組をまとめ、ENV に足す文字列を返す"""
    ex = ''.join(dict.fromkeys(p[0] for p in parts))
    body = ','.join(p[1] for p in parts)
    beams = 'typeof beamsUpdate==="function"&&beamsUpdate(dt);'
    return ex + f"\nconst SPECIAL={{P:[{body}],reset(i){{this.P.forEach(p=>p.reset&&p.reset(i))}},update(now,dt){{this.P.forEach(p=>p.update&&p.update(now,dt));{beams}}}}};\n"


def space_env(pos=(-160, 60, -220), color='0xfff4e0'):
    """地球圏の宇宙。太陽は遠く小さく置く"""
    return env(color=color, glow='0xffe0b0', pos=pos, special='')


def land_env(low, high, water=None, amp=6, seed=1, sky='0x6f8297'):
    e = sky_env() + ground(low=low, high=high, amp=amp, seed=seed, water=water)
    return e.replace('0x6f8297', sky)


def wall(r=60, h=14, cx=0, cz=0, y=-4, color='0xb8b0a0', arc=6.2832, start=0):
    """円形の壁（進撃の巨人の城壁など）。arc で一部だけにもできる"""
    return f"""
(function(){{const g=new THREE.CylinderGeometry({r},{r},{h},120,1,true,{start},{arc});const m=new THREE.Mesh(g,new THREE.MeshLambertMaterial({{color:{color},side:THREE.DoubleSide}}));m.position.set({cx},{y}+{h}/2,{cz});scene.add(m)}})();
"""
