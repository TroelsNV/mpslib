// (c) 2015-2016 I-GIS (www.i-gis.dk) and Solid Earth Geophysics, Niels Bohr Institute (http://imgp.nbi.ku.dk)
//
//    This file is part of MPSlib.
//
//    MPSlib is free software: you can redistribute it and/or modify
//    it under the terms of the GNU Lesser General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//
//    MPSlib is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU Lesser General Public License for more details.
//
//    You should have received a copy of the GNU Lesser General Public License
//    along with MPSlib (COPYING.LESSER).  If not, see <http://www.gnu.org/licenses/>.
//
#include <iostream>
#include "ENESIM_GENERAL.h"

int main(int argc, char* argv[]) {

  std::string parameterFile;

  if (argc>1) {
    parameterFile = argv[1];
  } else {
    parameterFile = "mps_genesim.txt";
  }

  MPS::ENESIM_GENERAL aSimulation(parameterFile);

  aSimulation.startSimulation();

  return 0;
}
