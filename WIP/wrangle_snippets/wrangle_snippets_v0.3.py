//Camera Frustrum

vector ndc = toNDC(ch("camNode"),@P);
float ov = chf("padding");
if(ndc[0]-ov&lt;0||ndc[0]+ov&gt;1||ndc[1]-ov&lt;0||ndc[1]+ov&gt;1||ndc[2]&gt;0)
{
removepoint(0,@ptnum);
}





//Threshold Deleter

if(ch("randtgl")==0)
{
if(@`chs("channelname")`&lt;chf("deletevalue"))
removepoint(0,@ptnum);
}
else
{
if(rand(@`chs("channelname")`+chi("seed"))&lt;chf("deletevalue"))
removepoint(0,@ptnum);
}






//Attribute visualizer
@Cd=set(0,0,0);
@Cd[0]=@`chs("attribute_to_visualize")`*chf("visualization_multiplier");




//dual clusters
int pt0 = vertexpoint(0,primvertex(0, @primnum, 0));
int pt1 = vertexpoint(0,primvertex(0, @primnum, 1));

int cluster0 = point(0, "cluster", pt0);
int cluster1 = point(0, "cluster", pt1);

if(cluster0 == cluster1){
    s@constraint_name = "Glue_Inside";
} else {
    s@constraint_name = "Glue_Outside";
}

f@strength = 1;
f@impulse_halflife = 0.1;
f@propagate_rate = 1.0;








//copy rbd position to constraint position
int pt = findattribval(1, "point", "name", @name);
@P = point(1, "P", pt);





//acceleration intensity
//group set to  !broken (prim)
float accel = length(v@force) / @mass;

if(accel > ch("max_accel_threshold")){
    @group_hi_activate = 1;}
else if(accel > ch("min_accel_threshold")){
    @group_low_activate = 1;}




//group broken
if(@group_low_activate && s@constraint_name = "Glue_Outside"){
   @group_broken = 1; }
else if(@group_hi_activate){
   @group_broken = 1; }

   
   
   
   
 //Attribute transfer by pcopen  
   float maxradius = 0.2;
vector nb_color;
float dist;
 
int handle = pcopen(@OpInput2, "P", @P, maxradius, 10);
 
while(pciterate(handle))
{
    pcimport(handle, "Cd", nb_color);
    pcimport(handle, "point.distance", dist);
    @Cd = lerp(@Cd, nb_color, dist/maxradius);
}