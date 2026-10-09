// Heuristic best-response search only. A returned witness is exact-checkable;
// failure to find one is NOT an exhaustive bound.
#include <array>
#include <cstdint>
#include <iostream>
#include <random>
#include <cmath>
#include <set>
using U=uint64_t;
using Bits=std::array<U,4>;
Bits mon[37], layers[9], target;
Bits eval(U c){Bits v{};for(int i=0;i<37;i++)if(c>>i&1)for(int k=0;k<4;k++)v[k]^=mon[i][k];return v;}
std::array<int,9> counts(Bits v){std::array<int,9> a{};for(int w=0;w<9;w++)for(int k=0;k<4;k++)a[w]+=__builtin_popcountll((~(v[k]^target[k]))&layers[w][k]);return a;}
int main(int argc,char**argv){
 double q[9]; for(int w=0;w<9;w++)if(!(std::cin>>q[w])) return 2;
 int restarts=argc>1?std::stoi(argv[1]):2000;
 std::mt19937_64 rng(argc>2?std::stoull(argv[2]):20261009);
 for(int x=0;x<256;x++) {U bit=U(1)<<(x%64);int k=x/64;int w=__builtin_popcount((unsigned)x);layers[w][k]|=bit;if(w%3==0)target[k]|=bit;
  mon[0][k]|=bit;for(int i=0;i<8;i++)if(x>>i&1)mon[1+i][k]|=bit;
  int z=9;for(int i=0;i<8;i++)for(int j=i+1;j<8;j++,z++)if((x>>i&1)&&(x>>j&1))mon[z][k]|=bit;
 }
 int sizes[9]={1,8,28,56,70,56,28,8,1};for(int w=0;w<9;w++)q[w]/=sizes[w];
 auto score=[&](Bits v){auto a=counts(v);double s=0;for(int w=0;w<9;w++)s+=q[w]*a[w];return s;};
 std::set<std::array<int,9>> seen;
 std::uniform_real_distribution<double> uniform(0,1);
 for(int r=0;r<restarts;r++) {
  U coef=rng()&((U(1)<<37)-1); Bits v=eval(coef); double s=score(v);
  // Random restarts and annealing find columns; no completeness claim.
  for(int step=0;step<500;step++) {
   int b=rng()%37;Bits vv=v;for(int k=0;k<4;k++)vv[k]^=mon[b][k];double ss=score(vv);
   double t=0.035*std::pow(0.002,step/499.0);
   if(ss>=s || uniform(rng)<std::exp((ss-s)/t)){v=vv;s=ss;coef^=U(1)<<b;}
  }
  // finish at a single-coordinate local maximum
  for(int it=0;it<50;it++) {int b=-1;double bs=s;Bits bv;
   for(int j=0;j<37;j++){Bits vv=v;for(int k=0;k<4;k++)vv[k]^=mon[j][k];double ss=score(vv);if(ss>bs+1e-12){bs=ss;bv=vv;b=j;}}
   if(b<0)break;coef^=U(1)<<b;v=bv;s=bs;
  }
  auto a=counts(v);if(seen.insert(a).second){std::cout<<coef;for(int z:a)std::cout<<' '<<z;std::cout<<'\n';}
 }
}
