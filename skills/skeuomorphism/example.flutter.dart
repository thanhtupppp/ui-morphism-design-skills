import 'package:flutter/material.dart';

class SkeuomorphicControl extends StatelessWidget {
  const SkeuomorphicControl({super.key, this.onPressed});

  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final compact = constraints.maxWidth < 600;
        final outerPadding = compact ? 6.0 : 8.0;
        final radius = compact ? 8.0 : 10.0;

        return DecoratedBox(
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [Color(0xFFD9D4C7), Color(0xFFAAA397)],
            ),
            border: Border.all(color: const Color(0xFF756F66)),
            borderRadius: BorderRadius.circular(radius),
            boxShadow: const [
              BoxShadow(color: Color(0x47000000), offset: Offset(0, 4), blurRadius: 8),
            ],
          ),
          child: Padding(
            padding: EdgeInsets.all(outerPadding),
            child: FilledButton(
              onPressed: onPressed,
              style: FilledButton.styleFrom(
                minimumSize: const Size(44, 44),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(6)),
              ),
              child: const Text('Activate'),
            ),
          ),
        );
      },
    );
  }
}
