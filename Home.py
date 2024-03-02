# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

from uihelpers import sidebar

LOGGER = get_logger(__name__)


def run():
    # sidebar.sidebar_head()

    st.set_page_config(
        page_title="Tadka95",
        page_icon="images/favicon.ico",
        layout="wide",
    )

    st.write("# Welcome to Tadka95! 👋")

    st.image("images/tadka95_squarelogo.png", use_column_width=True)
    st.markdown(
        """
        Welcome to Tadka 95, where Indian and international cuisines meet creativity. Our dishes, a blend of tradition 
        and innovation, will redefine your flavor palette. Prepare for an unexpected culinary adventure that’s more 
        delicious than you could ever imagine. Get ready to be tempted!
        - Check out [Harshit Yadav](https://harshityadav.in)
        - Github Repo [Tadka95](https://github.com/harshityadav95/Tadka95/)
        
        ### My Cooking Style Inspirations
        - [J. Kenji López-Alt](https://www.youtube.com/@JKenjiLopezAlt)
        - [CookingShooking](https://www.youtube.com/@CookingshookingIn)
        - [Chef Ranveer Brar](https://www.youtube.com/@RanveerBrar)
    """
    )


if __name__ == "__main__":
    run()
