using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormsUITest
{
    public partial class frmMain : Form
    {
        public frmMain()
        {
            InitializeComponent();
        }

        private void menuFile_Click(object sender, EventArgs e)
        {
            
        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Hei siellä! Miten menee?", "Hei siellä!", MessageBoxButtons.OK);
        }

        private void btnTest_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Test pressed!", "Press", MessageBoxButtons.OK);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("button1", "Press", MessageBoxButtons.OK);
        }
    }
}
