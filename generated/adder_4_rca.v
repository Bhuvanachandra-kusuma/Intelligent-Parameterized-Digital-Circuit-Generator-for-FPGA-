module cla_4bit(
    input [3:0] A, B,
    input Cin,
    output [3:0] SUM,
    output Cout
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

endmodule


module adder_4_cla(
    input [3:0] A, B,
    output [3:0] SUM
);

    wire Cout;

    cla_4bit u0(A, B, 1'b0, SUM, Cout);

endmodule
