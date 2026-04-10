module cla_4bit(
    input [3:0] A, B,
    input Cin,
    output [3:0] SUM,
    output Cout,
    output P_group,
    output G_group
);

    wire [3:0] P, G;
    wire [4:0] C;

    assign C[0] = Cin;

    assign P = A ^ B;
    assign G = A & B;

    assign C[1] = G[0] | (P[0] & C[0]);
    assign C[2] = G[1] | (P[1]&G[0]) | (P[1]&P[0]&C[0]);
    assign C[3] = G[2] | (P[2]&G[1]) | (P[2]&P[1]&G[0]) | (P[2]&P[1]&P[0]&C[0]);
    assign C[4] = G[3] | (P[3]&G[2]) | (P[3]&P[2]&G[1]) |
                  (P[3]&P[2]&P[1]&G[0]) |
                  (P[3]&P[2]&P[1]&P[0]&C[0]);

    assign SUM = P ^ C[3:0];
    assign Cout = C[4];

    assign P_group = &P;
    assign G_group = G[3] | (P[3]&G[2]) | (P[3]&P[2]&G[1]) | (P[3]&P[2]&P[1]&G[0]);

endmodule


// 🔥 THIS MODULE NAME IS CRITICAL
module adder_8_cla(
    input [7:0] A, B,
    output [7:0] SUM
);

    wire [1:0] P_group, G_group;
    wire [2:0] C;
    wire Cout0, Cout1;

    assign C[0] = 1'b0;

    // carry between blocks
    assign C[1] = G_group[0] | (P_group[0] & C[0]);

    cla_4bit b0(A[3:0], B[3:0], C[0], SUM[3:0], Cout0, P_group[0], G_group[0]);
    cla_4bit b1(A[7:4], B[7:4], C[1], SUM[7:4], Cout1, P_group[1], G_group[1]);

endmodule
