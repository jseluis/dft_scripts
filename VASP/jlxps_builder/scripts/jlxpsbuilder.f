 14   PROGRAM FORTPLANTA

      real X(1:50000),Y1(1:50000),start,end,A,C,X_IN(1:50000)
      REAL STEP,Y1_IN(1:50000),Y2_IN(1:50000),Y3_IN(1:50000)
      real fwhm,ytot(1:50000),y(1:50000)
      INTEGER i,J,NPEAKS


      read(5,*)npeaks,start,end,fwhm
      c=2.772588722/(fwhm**2)

***READ IN DISCRETE SPECTRUM***
      DO 10 i=1,Npeaks    
         read(5,*,err=10)x_in(i),y1_in(i)
C         y1_in(i)=y1_in(i)*y1_in(i)
C         y2_in(i)=y2_in(i)*y2_in(i)
C         y3_in(i)=y3_in(i)*y3_in(i)
         ytot(i)=y1_in(i)
 10   CONTINUE
      
***CREATE GAUSSIAN***
C      start=355.
C      end=380.
      step=0.05
      I=1
      x(1)=start
      A=1.
 20   if (x(I).lt.end) then
         i=i+1
         x(i)=x(I-1)+step
         y(i)=0
         do 25 j=1,npeaks 
            y(i)=y(i)+ytot(j)*A*exp(-c*(x_in(j)-x(i))**2)
 25      continue
         write(6,*)x(i),y(i)
         GOTO 20
      endif




         stop
         end
               









