"""
Copyright 2017 Oliver Smith

This file is part of pmbootstrap.

pmbootstrap is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pmbootstrap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pmbootstrap.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import pmb.challenge


def frontend(args):
    path = args.challenge_file
    if path.endswith(".apk"):
        pmb.challenge.build(args, path)
    elif os.path.basename(path) == "APKINDEX.tar.gz":
        pmb.challenge.apkindex(args, path)
    else:
        raise ValueError("It is only possible to challenge files ending"
                         " in .apk or files named APKINDEX.tar.gz.")
